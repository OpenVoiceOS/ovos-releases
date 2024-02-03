# Overview

This repository contains submodules for all the git repos that form an OVOS release.

It provides a convenient way for developers to work on OVOS as a whole and a reliable way to define the code contained in a release.

As such the main use of the ovos-releases repo will be
1. for developers to track ongoing collaborative work by simply pull/updating all submodules
2. for users and/or testers to obtain fixed snapshots of OVOS as a whole.

This is currently a proposal/wip and is intended to be expanded and refined.

## Releases
Releases will be represented by a tag in this ovos-releases repo.

This will identify the exact commit in each submodule that will be used for that release.

# OVOS individual repository branches

Individual OVOS repos will have four types of branches: dev, testing, feat/*, WIP/*

## dev
Normal bug fixing and incremental work
## testing
Tracks dev as closely as possible. Conceptually when tests succeed. dev -> testing PR would be triggered by a human, and can include any number of PRs to dev (eg, feature + bug fixes introduced), once test in that PR pass and reviewers approve it becomes testing. This layer also gives more protection rules, like requiring 2 approvals for testing etc, while dev would not require approvals at all depending on the repo.
## feat/*
As described in ovos-releases
## wip/*
Known breaking development (eg API changes or collaboration branches).


# ovos-releases branches


There will be three types of branches in ovos-releases: release-candidate (rc/) and feature (feat/).

## Alpha branch

The alpha branch is the development branch for and will automatically be kept up-to-date with the dev branches of all submodules.

## Release branches : rc/$R

The rc/$R branch is the development branch for working towards release $R and, post-release, for providing point-release updates.

The rc/$R branch will automatically be kept up-to-date with the testing branches of all submodules.

Release candidates (testing points) and releases are tagged on the rc/$R branch.

After a release, the rc/$R+1 branch will be created and will become the new default branch.

The (now-old) rc/$R-1 branch may have bug fixes applied and subsequent point releases may be tagged along the 'old' rc/$R-1 branch.

Submodules will not generally need to have rc/$X branches. If bug fixes are required after a release $X and the repo has commits that are not desired in the release then they will have an rc/$X branch created at the sha1 of the submodule in ovos-releases at the release tag. Bug fixes will be applied to this branch and the rc/$X branch in ovos-releases will have the submodule sha1 updated. Point release tags would then be made on the rc/$X branch.

## Feature Branches

All changes that involve more than one repo should be co-ordinated in a feature branch in ovos-releases.

This will allow cross-repo pip version dependencies and API changes to be contained in the scope of that branch.

That feature branch is then added to all repos that need to be modified.

Once work on the feature branch is complete (ie at least enough that it is accepted into general development) then it can be merged to rc/$R on ovos-releases and this process will merge the feature branches on all submodules to testing too (ie this could be automated). Alternatively the feature branches on all relevant submodules could be merged to testing and then they would automatically be picked up by rc/$R.

Each feature should have a relevant issue in https://github.com/OpenVoiceOS/ovos-releases/issues to track activity and provide information about the feature. Then the developer can request a feature branch in ovos-releases on the issue. (Because Github doesn't allow a PR to a non-existant branch afaik).

(See https://github.blog/changelog/2022-03-02-create-a-branch-for-an-issue/ and https://github.com/marketplace/actions/create-issue-branch for ideas on how to simplify this)

The branch should be named feat/{issue#}_{name}

Feature branches in ovos-releases are NOT expected to be functional. It may be the case that some submodules have outstanding PRs or the feature may simply be in a WIP status.

Note: It may be appropriate for breaking changes that only affect one repo to be pushed to a WIP branch in a submodule. This will avoid being pulled into the rc/$R branch until it's ready. This doesn't need to be a feature branch for a single repo but there's no reason it can't be.

# Updates from submodules

How does a change in a submodule get accepted into ovos-releases.

First clone ovos-releases (you're probably doing that anyway)

1. Normal development on a single repo (eg bug fix, isolated feature)
   1. Work on the dev branch in the submodule
   1. Test and commit changes
   1. Submit PR to submodule repo
   1. PR approved
   1. Updated submodules in ovos-releases
   1. Commit with a suitable message
   1. Submit PR for ovos-releases
   
   The last 3 steps should be automated when a PR is approved to any submodule testing branches. This automation should appropriately update all feature branches too
   
1. Normal development on multiple repos (eg bug fix, distributed feature, pip dependency changes)
   1. Create an issue on ovos-releases for the feature. Note that this can be done at any time should the developer realise that multiple repos are impacted.
   1. Request feat/$F branch in the ovos-releases issue (for each submodule too)
   1. Create and checkout the feature branch (feat/$F) in each submodule.
   1. Work on the feature branch in the submodules
   1. Test and commit changes
   1. Submit PR to each submodule repo for the feat/$F branch
   1. PRs approved
   1. Updated submodules in feat/$F ovos-releases. At this point all non-involved repos are on the 'testing' branch and involved repos are on the feat/$F branch.
   
   Could we automate on any PR to any submodule on branch == feat/$F
   
   Note: submodule feature branches must be manually kept up-to-date (rebase etc) with submodule testing branches.
   
   Note: It would be tricky for normal users to test with multiple features at once as that's complex and would proably need a local merge of feature branches.
   
# Release process

TBD

