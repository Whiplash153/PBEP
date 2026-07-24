# 02. VPS

## Goal

Learn how to connect to a remote Linux server via SSH, navigate Ubuntu, and prepare a VPS for application deployment.

---

# What is a VPS?

A **VPS (Virtual Private Server)** is a virtual machine running in a data center that is accessible over the Internet.

Unlike a local computer, a VPS can run 24/7 even when your personal computer is turned off.

---

# SSH

**SSH (Secure Shell)** is a secure protocol for remotely managing a server through a terminal.

Connection command:

```bash
ssh username@IP
```

Example:

```bash
ssh root@147.90.10.132
```

After connecting, commands are typed on the local computer but executed on the remote server.

---

# Choosing a VPS

The following configuration was selected for learning:

- Ubuntu 24.04 LTS
- 2 vCPU
- 2 GB RAM
- 60 GB SSD
- IPv4

This configuration is sufficient for learning Linux, Docker, FastAPI, and application deployment.

---

# First SSH Connection

On the first connection, SSH asks to verify the server's fingerprint.

After confirmation, the server is added to:

```text
~/.ssh/known_hosts
```

Future connections to the same server no longer require confirmation.

---

# Exploring Ubuntu

The following basic Linux commands were used:

```bash
pwd
whoami
ls
ls -la
cd /
date
```

The main Linux directories were explored:

- `/`
- `/root`
- `/home`
- `/etc`
- `/usr`
- `/var`
- `/tmp`
- `/dev`
- `/bin`

---

# Git

Checking whether Git is installed:

```bash
git --version
```

Git was already included in the Ubuntu image.

Git is used to clone and update projects from remote repositories such as GitHub.

---

# Working with APT

Before installing new software, the package index was updated:

```bash
apt update
```

Difference between the commands:

- `apt update` — updates the package index.
- `apt install` — installs the selected package.

---

# Docker

Checking whether Docker is installed:

```bash
docker --version
```

Docker was not installed and was added with:

```bash
apt install docker.io
```

After installation, Docker was verified using:

```bash
docker --version
docker ps
```

An empty `docker ps` table indicates that Docker Engine is running correctly, but no containers have been created yet.

---

# Docker Compose

Checking whether Docker Compose is installed:

```bash
docker compose version
```

Docker Compose was not installed and was added separately:

```bash
apt install docker-compose-v2
```

Verification:

```bash
docker compose version
```

Docker Compose was installed successfully and is ready for use.

---

# Result

The VPS is fully prepared for application deployment.

Installed and configured:

- SSH
- Ubuntu
- Git
- Docker
- Docker Compose

The server is now ready to host applications.