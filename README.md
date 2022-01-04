# report-build

---

## 🔴 This is a public repository 🔴

---
### Description
This is a Bitrise step to collect release information and send it to Tombstone Service.

### Prerequisites
- `PROD_TOMBSTONE_URL` needs to be set as an env var
This can be done as such:
```yaml
- app:
     envs:
        - opts:
              is_expand: false
          PROD_TOMBSTONE_URL: "https://INSERT_URL_HERE"
```
---
### Usage
- Add a step call within the desired workflow of your `bitrise.yml` to report the new release:
```yaml
- git::https://github.com/WhoopInc/bitrise-report-release.git@main:
     title: Send mobile release to Tombstone Service
     inputs:
        - url: $PROD_TOMBSTONE_URL
        - version_code: "$XCODE_BUNDLE_VERSION"
        - version_name: "$XCODE_VERSION_NAME"
        - branch: "$BITRISE_GIT_BRANCH"
        # This will be the name of the app being released, either "IOS" or "Android".
        - release_name: "..."
        # This will be the type of app being released, either "IOS" or "ANDROID".
        - mobile_platfrom: "..."
        - auth_token: "..."
     is_always_run: true
     is_skippable: false
```
