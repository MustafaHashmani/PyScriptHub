import hashlib
import sys
import requests


def request_api_data(query_char):
    """Takes the first 5 Characters of the
    hashed password and returns a response to the pwned API"""
    url = "https://api.pwnedpasswords.com/range/" + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f"Error fetching {response.status_code}, check the API and try again"
        )
    return response


def pwned_api_check(password):
    """Converts the password into SHA1 HASHED,
    passes the first 5 Characters into request_api_data
    for security reasons and returns the number of times the password was leaked
    """
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def get_password_leaks_count(hashes, hash_to_check):
    """Searches for the password in the response
    and returns the number of times it was leaked
    , if found"""
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def main(args):
    """Searches for every password in the response
    from the API and prints an appropriate response"""
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f"{password} was found {count} times ... you should probably change your password"
            )
        else:
            print(f"{password} was not found. Carry On!")


if __name__ == "__main__":
    main(sys.argv[1:])
