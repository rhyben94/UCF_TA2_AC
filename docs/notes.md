#### Engineering notes

###### Build and push agent to ASIST registry
 * `./agent.sh build`
 * Increment `LAUNCHER_TAG` value as appropriate in settings.env
 * Verify differences between TESTBED repo `./bin/check_with_testbed.sh`
 * Update TESTBED repo. `./bin/update_testbed.sh`
 * Update the newly built image `./src/ucf-release-to-aptima.py --upload_images`
 * In TESTBED repo, update `releaseNotes.md`
 * Commit and push changes to branch in TESTBED repo
 * Create merge request for TESTBED repo.
 * Commit and push changes in this repo.