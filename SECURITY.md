# Security Policy

## Reporting a vulnerability

**Please do not report security issues in public issues, pull requests, or discussions.**

Report privately, either way:

- **Preferred — GitHub private vulnerability reporting.** Check this repository's **Security** tab for **Report a vulnerability**. If it's not offered, this repo doesn't have it enabled yet — use email instead.
- **Email — `whitetalonindustries@gmail.com`.** Works whether or not GitHub reporting is enabled here, and for anyone without a GitHub account.

We do not currently publish a PGP key. If you need encrypted transport for a report, say so in a message with no technical detail and we will arrange it.

### What to include

- The project and the version or commit.
- What an attacker can do, in one sentence.
- Steps to reproduce, with the smallest input that shows the problem.
- Your platform, if it matters.
- Whether anyone else knows, and whether you have a publication date in mind.

**Please do not send real personal data from anyone's actual install as a proof of concept.** Synthetic data demonstrates the bug just as well. If the problem can only be shown with real data, tell us that rather than sending it, and we will work out a safe reproduction together.

## What you can expect

| Stage | Our commitment |
| --- | --- |
| Acknowledgement | within 5 business days |
| Triage — reproduced, severity assigned, timeline shared with you | within 10 business days of acknowledgement |
| Updates while open | at least every 14 days |
| Fix — critical | 30 days from triage |
| Fix — high | 60 days from triage |
| Fix — moderate | 90 days from triage |
| Fix — low | next scheduled release, best effort |
| Public advisory | at fix release, or 90 days from triage, whichever is first |

These are deliberately modest. We are a small team with no 24/7 security contact, and we would rather publish numbers we hit than numbers that sound good. If we are going to miss one, we will tell you before it passes, with a reason and a new date.

## Scope

**In scope:** code in this repository; released binaries, packages and installers, and the pipeline that builds them; default configuration and default behaviour; how the software stores, logs, caches, backs up or transmits user data; our dependencies as we ship them; documentation that tells you to do something unsafe.

**Also in scope, and the report we most want:** any place our README, UI, or release notes claim something is encrypted, private, local-only, or secure and it is not. We treat a false security claim as a vulnerability.

**Out of scope:** third-party services and platforms we do not run; attacks requiring an already-compromised OS, existing root access, or physical access beyond what the project's threat model covers; denial of service and volumetric testing; social engineering and phishing; scanner output with no demonstrated impact; missing hardening with no exploit path; dependency CVEs where the vulnerable path is not reachable in our release.

If you are not sure, send it anyway. We would rather triage something out of scope than miss something in it.

## What we ask, and what we promise

We ask you to give us a reasonable chance to fix the problem before publishing, to test only against your own installation and your own data, to stop as soon as you have demonstrated the issue, and not to access or keep data that is not yours.

In return, we will treat good-faith research under this policy as authorised, work with you on timing, credit you however you want to be credited — including not at all — and show you the advisory before it goes out. We will not publish your name or contact details without your say-so.

If we have not fixed the issue and have not agreed a new date with you, you are free to publish 90 days after triage. We will not hold that against you.

## No bug bounty

**We do not run a bug bounty and we do not pay for vulnerability reports.** No reward, no swag, no exception for critical findings. We are saying so plainly so that nobody spends a weekend on our code expecting to be paid. What you get is a fast honest answer, a fix, a public advisory, and credit.

## Why this matters here

White Talon Industries maintains this project alongside several other public and private repositories. A flaw here is not an abstraction to the people who use it. Thank you for taking the time to tell us about one privately.
