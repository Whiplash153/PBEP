# Dockerfile

## Goal

Learn how to create custom Docker images using Dockerfile and understand the purpose of the main Dockerfile instructions.

## What was done

Created custom Docker images based on Ubuntu and Python images.

Worked with FROM, RUN, WORKDIR, COPY, CMD and ENV instructions.

Built and rebuilt images multiple times.

Copied files into images and executed Python code inside containers.

Used environment variables inside Docker images.

## Notes

Dockerfile is a recipe for building an image.

Changing Dockerfile does not change an existing image until a new build is performed.

RUN is executed during image build.

CMD is executed when a container starts.

COPY transfers files from the local machine into an image.

WORKDIR sets the working directory inside the image.

ENV creates environment variables inside the image.

Using specialized base images such as `python:3.12` simplifies image creation.