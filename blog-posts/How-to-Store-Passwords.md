---
title: How to Store a Passwords
date: 2023 Nov 2
---
**Disclaimer**: The world of cyber-security is an incredibly complex and constantly evolving topic, and I am not a cyber-security researcher; I create projects for fun.

Storing a password in a server can be intimidating. Password management is incredibly tricky, as anything you mess up could compromise your users' password(s). Thankfully, random websites you've never visited before have a pure HTML blog post from 2023 about that exact topic, and how to do it properly.

Basically, it's just this sequence of steps:

* Generate a long random sequence of characters, this is called a *[salt](https://en.wikipedia.org/wiki/Salt_(cryptography))*(generate for each user, do not use a master salt)
* Prepend(or append, it doesn't matter, just keep it consistent) this to the user's password
* Use a [hashing algorithm](https://en.wikipedia.org/wiki/Hash_function), such as [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2), to generate a unique sequence of characters that will uniquely identify that password.
* Store the salt and hash in the same place, *do not* store the password on it's own.

And to check if a password is right, repeat the steps, except rather than generating a random sequence of characters, get the sequence of characters that you've stored along with the hash.

## Why Do *This*?
You might be thinking: *That's a bit arbitrary innit?* And if you aren't then you can stop reading now.

This method of storing passwords is the only way to ensure that you are securely storing them. So let's go through some other ways, and why they aren't so good.

### Plaintext Passwords

Storing your passwords in plaintext allows anyone who can get into your server to easily take any password they want, as no matter how good your users' password is, their account will be hacked if an unauthorized or malicious individual is able to get in.

### Encrypted Passwords

This is basically just plaintext with additional steps. As long as your master-key is stored somewhere, it will get stolen as soon as somebody manages to get into your system.

### Bare Hashing

A hash isn't able to be undone, meaning theoretically you should be able to *just* hash your password. This, while a fair assumption, has unfortunately been incorrect for quite some time. There are databases online that store every word in the english language(or just some words) in addition to common passwords and their hashes, and users will often use words for their passwords, even though it's insecure.

This is where salts come in. Due to the nature of hashes, even a single change in a string will entirely change it's hash, as such, if you add a random sequence of characters to a string, then you can entirely change it's hash.