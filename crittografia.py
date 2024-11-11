
# creazione environment, per evitare che ubuntu non vi faccia installare la libreria di crittografia
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# # Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# Per iniziare generiamo una coppia di chiavi e le stampiamo
# Generating RSA Key Pair
# Una volta stampate, non serve più
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())
# public_key = key_pair.publickey()
# print(public_key.export_key())
# exit(0)
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAuiDrw4Y59HsMijMIWkSyhJauRnfRXMf4mmcG7DmJdtN46lqo\ndzUpA4PsIxE5NKc/0zQIfE5Sx+RqAJBwLQ76+92sGmjrDT4oq/68Xu24gY7K2Kl9\ndXuDxYsXJMgm5FpNQV1fTDLG1uLNbVrAlPrnzLO1p15vO7GDHhmNSJU3F2jgbtwN\nh9znDlLnkkT4AKjdtOQKy+ZmdafzXHmTdnRwvZNWPPrOwms4sh868NcXM+zknpNU\ncJ23uTwqtcTHEtIti7Eok4kpj3iY16h9301mH0AQ15ga15RsigHRTn3PxjqwDW3E\ngo3Jy+seu7qbuLIhuhnFJeZMlAmvj7mvg9Ar9QIDAQABAoIBACKLJ5ZjG/BuwdYI\nQJ2YMFWBLZjwdc+1YUMuqc8/om6GMuOzrZ5qJFF9s16SvL4z6BmHh6eiVaS5lJ7E\nL719EUGbU2yXWkBb7+pz3Xv0vJB28tihJCKgqMUJ2mK+LtGknL/r11rp9ZM+Bogs\nFp/PrSOFmsoUMaqveDkm3tzArLfQMwa/8SDeQ882tSVo5nTEVPdGC+xO3PluaC0K\n8l0Cy/5FJrJeGz7aIR1rHH1dzo/mMkYw6mOL2h/9Yc+PIH5HcUKy4LyW4CzJOFUW\nLlYACBeKFh+VyNacr7QVORM5SLtUKBWJWnqU48/xWdAoOiC632/NUrWyNE89hpFd\nT49KVaUCgYEA11OC8ye4Asnf2JWF+XMATOAOYi/3MVmv89+v7b6EWTQelW39zamL\n3p4AygZtL+jyTtnljjvq8fhfdKSpxt9lm7WudReFYJmgbiFT6D0UqmjRHqUY9b3P\nd4OyM3HWg3AmsshuR0gB1nVVB3Ru5bbVkbYtp5GpSiKRlbxCqMySOrcCgYEA3UmB\neX4xCvarFEntEeyLdnedf/rnqqHHw/oUnBnItkveQ8E6N+fS9KOzJKaXtEezVfcg\nIkH0AWJT0qaFxfmhEllCbHCCjwYbEvw9O+eWE6MGHarI4uCHw/0tjv43c/oKPFWI\nNogeqfhqp3a8XzVivImZg74wC1DewNb7gBrR0rMCgYBVJuxpNjLZv3WrU+4oaKcc\nv5pQkAFkXcBsY/BRx37VO/xAQcAV3c+3WKqdOg9h2/A+6IKUTfOqfvtYyGlvgRbQ\njfeQzJ1tRzOfecSR2d3bShow0T9epxJthAIrwAAB+I8FMqgRvlMjuUDH8u6MH1K0\nDeReGQdmjucd3NZLpKLLXwKBgQCAPmJP48dOYEgjmPhQg/MLNCVODz4FkH6yYBNj\nqDm/FFb6k1hHIA4NA3YFzppqu4b+UhsIX4qm5rJHiYRLiPFFLf+l0sqHUvWL2i0u\ns3cxaDBaLyj++zsTZX3quf+vMgCOmM85M0f6H2LILLLcxpazR1d1l1pGpJaD0dOt\nmV1yqwKBgQCQpiwWxfKNWjWVjvHsMtGoJNvObOCSKr1XvFn1t4Q0UJu8xLK8Q4lf\nRXtd4YhB/jIuSgnx5sEbUiLSfk4gxLkb2byc07b7t4WT2zOWlLb6PGLLghiCuE2W\nbGYv69F6dFBwfezJXJWyL5zhTMxRq4CPUW+nNif1ncO8bt/cDWPALQ==\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuiDrw4Y59HsMijMIWkSy\nhJauRnfRXMf4mmcG7DmJdtN46lqodzUpA4PsIxE5NKc/0zQIfE5Sx+RqAJBwLQ76\n+92sGmjrDT4oq/68Xu24gY7K2Kl9dXuDxYsXJMgm5FpNQV1fTDLG1uLNbVrAlPrn\nzLO1p15vO7GDHhmNSJU3F2jgbtwNh9znDlLnkkT4AKjdtOQKy+ZmdafzXHmTdnRw\nvZNWPPrOwms4sh868NcXM+zknpNUcJ23uTwqtcTHEtIti7Eok4kpj3iY16h9301m\nH0AQ15ga15RsigHRTn3PxjqwDW3Ego3Jy+seu7qbuLIhuhnFJeZMlAmvj7mvg9Ar\n9QIDAQAB\n-----END PUBLIC KEY-----"
sPubEd = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn1Q4/NisrrEa/Su+tTER\nKnsTelXHanenIe8nYbudpY9ymyXJ5SZDLVivQZ8Ml0g0ivNQ134ZzqGkMt8COK5o\ndoworlmpDFCU+w5HmOlyy91/NPJ1LFSUV2B4GJhCBcGeK4VtKhimpDdWLiuo9E3I\n+GF7QAOFvt+4lCY1xycUHkzrVXuILKOjYahZf0hPs6CeoySeVKvhIhb1u4yJLlbQ\ngeQUyOs420rgHiUf+OxJ5n+KKWZe9NmwyHro37P631BCJtZM/Iov8im9/y9TWraF\nZP59QOUbjcUokv0YOK8b31MkNeA/t9LPQg2lTpaCTpbwJ1NmYA2uWD+WGCJm3Aem\ngQIDAQAB\n-----END PUBLIC KEY-----"
# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)
public_key_Ed = RSA.import_key(sPubEd)


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
# message = "This is a secret message"
# encrypted_message = encrypt_message(message, public_key)
# decrypted_message = decrypt_message(encrypted_message, key_pair)

# print("Original Message:", message)
# print("Encrypted Message:", encrypted_message)
# print("Decrypted Message:", decrypted_message)

encrypted_message = "SgrNIP6iTwSr9mG3TeuvKkl9xReWnko3MT6e8RFsW5KxjOtDUVdYz/unuBr604lA/ve+RsRFPYT9Gq+/5AQe7/DWWZ9nwokP/kUR6/TYMdYkg9BZDt68B+3eiRlOJUy1yxUj3lbKAc55YVTIehfRkhgqocieP904FGZhVytFf20fkVp3r4GvI5RDCH7bHmR/J9OBjsbUCB6lkDJdzFXdTSoQMcX+kZ7Jw9k81pSFbJF/jaTiceE3zZpqKku3WgczMG4gPMEpe3l5HBx6WBFgC8FPBQMmsXk4iSku8+3MpuFmlruJ7MaVs5dVL7dIupgcl8rHzTypoyyA64H4OElPJw=="
decrypted_message = decrypt_message(encrypted_message, key_pair)

print(decrypted_message)

messrisp = "Ora sono in aula a studiare Sicurezza2 a Laurentina"
cifra = encrypt_message(messrisp, public_key_Ed)
print(cifra)
