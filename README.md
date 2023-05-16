# base62_token

Proof-of-concept for a GitHub[^1] / npm[^2] style token library in Python.

This may not fulfill the security requirements for a real world application.
Please do not use it in production.

## Usage

```python
import base62_token

token = base62_token.generate("prefix",32)
if base62_token.is_valid(token):
    ...
```

## Compatibility

The base62 algorithms used in `encode`/`decode` should be COMPATIBLE[^3] with saltpack / GMP / GnuPG. 

`generate` and `is_valid` are not designed to be compatible with anything else.

`is_valid_gh` verifies prefix and checksum for the old new GitHub tokens[^1].
`generate_gh` creates dummy tokens that should be indistinguishable from real ones without active validation.

## References
[^1]: https://github.blog/2021-04-05-behind-githubs-new-authentication-token-formats/
[^2]: https://github.blog/2021-09-23-announcing-npms-new-access-token-format/
[^3]: https://github.com/therootcompany/base62.js/issues/1

