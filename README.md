# Blango — Historical Django Course Project

> **Status:** Archived / historical learning project. This repository is retained for provenance and learning value; it is not an actively maintained production application.

Blango began as the starting point for an **Advanced Django** course and evolved beyond the initial `django-admin startproject blango` scaffold with authentication, blog, REST-framework and Django Allauth experiments.

## What it demonstrates

- Django 3.2-era project structure
- custom authentication model
- Django Allauth/social-auth experimentation
- Django REST Framework authentication/permissions
- Bootstrap/crispy-forms integration
- local SQLite-backed development

## Security and maintenance status

The current tree no longer commits the local SQLite database or a reusable development `SECRET_KEY`. Local databases and environment files are ignored going forward.

This code reflects an older course environment and should not be treated as a current Django production baseline. In particular, dependency versions, middleware/security settings, authentication configuration and deployment assumptions should be reviewed before any reuse.

## Archive policy

No feature development is planned here. If an implementation pattern remains useful, migrate the specific idea into an actively maintained project rather than reviving this repository wholesale.

Historical Git commits may still contain files removed during archive hygiene. The repository is retained for learning/provenance, not as a source of deployable secrets or runtime data.
