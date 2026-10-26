The meeting focused on a critical blocker for the planned ECB funding project testing on the TF1 application: the required "IAM-Server" authentication service is no longer available in the UAT environment, 
impacting the ability to validate the JWT (JSON Web Token) and thus preventing testing of TF1 after the DB restore. 
The team explored the proposed solution of migrating to the new "IAL Server", but this requires a code adaptation in TF1 which currently lacks assigned development resources, 
as no developments are foreseen for TF1 in 2025. 
This situation must be resolved urgently to move forward with the ECB finding Project. 

# DISCUSSED TOPICS
- **Critical testing blocker for TF1:** The planned tests for the ECB finding project on the TF1 application, scheduled after the DB restore, are blocked.
- **Authentication service unavailability:** The "IAM-Server" service, which TF1 uses for authentication and JWT validation, was found to be unavailable in the UAT environment as of Monday, October 20th.
- **Decommissioning timeline:** IAM-Server was active when TF1 was released to production in July, suggesting its decommissioning occurred sometime after September.
- **Proposed alternative:** The Authentication team proposed using the new "IAL Server" as a replacement for the unavailable IAM-Server.
- **TF1 incompatibility and resource constraint:** IAL Server is not compatible with ASIS, requiring a developer to adapt the TF1 code, but no development resources are currently allocated 
to TF1 for 2025.

# 2. KEY DECISIONS / GIVE AWAYS INFORMATION
No key decisions were formally recorded; the discussion primarily centered on identifying the critical blocker and the associated resource challenge.

# 3. ACTION ITEMS (Actions to be taken)

|What Needs to Be Done (Action) | Who is the Owner (Responsible) | Due Date|
| :--- | :--- | :--- |
|Investigate why the IAM-Server was decommissioned post-September without prior notification and confirm the exact date.| TF1 Team / MHY Team | TBD (To Be Determined) |

# 4. NEXT STEPS / NEXT MEETING
Next steps/meeting details were not finalized. The immediate priority is to address the resource constraint for the TF1 code adaptation.