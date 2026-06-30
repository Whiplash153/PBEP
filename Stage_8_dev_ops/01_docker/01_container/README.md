# Docker Containers, Images and Lifecycle

## Goal

Understand the core Docker model and the relationship between images, containers and registries. Learn how container lifecycle works and how Docker manages container state.

## What was done

Downloaded an image from Docker Hub and examined the difference between an image and a container. Created multiple containers from the same image and explored container startup, shutdown and restart behavior. Investigated how changes inside a container are stored and how container removal affects those changes.

## Notes

An image is a reusable template, while a container is a running instance created from that template. A container exists independently from the image and can preserve its state after being stopped. Removing a container removes its internal state, but does not affect the original image.