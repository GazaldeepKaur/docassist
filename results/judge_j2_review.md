# Judge review sheet

Read at least 10 of these yourself. Do you agree with the verdict? Note where the judge is lenient or wrong.

## q01 (direct): Do I have to give my SIN when I apply for a job?

**Answer:** You do not have to provide your SIN when applying for a job [protect_SIN.pdf, page 3].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The answer correctly states that you do not have to provide your SIN when applying for a job, which is supported by the retrieved context from protect_SIN.pdf, page 3.
- gold: [('protect_SIN.pdf', 3)]

## q02 (direct): What phone number do I call to report SIN fraud to the Canadian Anti-Fraud Centre?

**Answer:** You can report SIN fraud to the Canadian Anti-Fraud Centre by calling 1-888-495-8501 [protect_SIN.pdf, page 4].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The answer correctly provides the phone number to report SIN fraud to the Canadian Anti-Fraud Centre, and this information is supported by the retrieved context from page 4 of the document.
- gold: [('protect_SIN.pdf', 4)]

## q03 (direct): How do I apply for a Social Insurance Number for my newborn baby?

**Answer:** To apply for a Social Insurance Number (SIN) for your newborn baby, you need to follow these steps:

1. Complete the Registration of Birth form and sign the “Request for a Social Insurance Number for My Child” section at the bottom of the form. This section acts as the SIN application for your child.
2. Ensure that your child is under the age of one year and that you have not already submitted the Registration of Birth form.
3. Once the birth is registered, the information will be sent to Service Canada, and they will mail you your child's SIN. The SIN record will reflect your child's name as it appears on the Registration of Birth form [apply_newborn_SIN.pdf, page 1].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The assistant's answer is correct and complete according to the REFERENCE and all factual claims are supported by the RETRIEVED CONTEXT.
- gold: [('apply_newborn_SIN.pdf', 1)]

## q04 (direct): Can I apply for a SIN by mail instead of going in person?

**Answer:** Yes, if you do not live in Canada, you are eligible to apply by mail using the “Application for a Social Insurance Number - Information Guide for Applicants” form [apply_SIN.pdf, page 1].

- correctness: 0  | grounded: False  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The answer only addresses applying by mail for those not living in Canada, ignoring the conditions under which residents can apply by mail.
- gold: [('apply_SIN.pdf', 1)]

## q05 (direct): Which documents must a temporary resident show to get a SIN?

**Answer:** Temporary residents must provide one of the following documents to get a SIN: 
- A work permit issued by IRCC or CIC.
- A study permit issued by IRCC or CIC that states the permit holder “may accept employment” or “may work” in Canada, or is accompanied by a “confirmation to work off campus” letter issued by IRCC or CIC before February 11, 2015.
- A visitor record issued by IRCC or CIC stating that you are authorized to work in Canada or that was issued under specific regulations.
- A diplomatic identity card and a work authorization [apply_SIN.pdf, page 3].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The assistant's answer is correct and complete according to the REFERENCE and all factual claims are supported by the RETRIEVED CONTEXT.
- gold: [('apply_SIN.pdf', 3)]

## q06 (direct): What do I need if my SIN document is in another language and has been translated?

**Answer:** If your SIN document is in another language and has been translated by a certified translator, you must submit an attestation stating that the translation is a true and accurate version of the original text. If the document has been translated by a translator who is not certified, you must submit an affidavit signed by the translator in front of a commissioner for oaths or a commissioner for taking affidavits [apply_SIN.pdf, page 5].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The answer correctly states the requirements for translated SIN documents and is fully supported by the retrieved context.
- gold: [('apply_SIN.pdf', 5)]

## q07 (direct): What does a legal guardian need to provide to apply for a child's SIN?

**Answer:** A legal guardian must provide the following to apply for a child's SIN: an original or a certified copy of a document that confirms their legal guardianship, issued by a provincial or territorial authority (in Quebec, a notarized will is an acceptable document), and a valid primary document proving their identity [apply_SIN.pdf, page 4].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The assistant's answer correctly lists the required documents for a legal guardian to apply for a child's SIN, and all claims are supported by the retrieved context.
- gold: [('apply_SIN.pdf', 4)]

## q08 (direct): Which documents can a Canadian citizen use as proof when applying for a SIN?

**Answer:** I don't know based on the provided documents.

- correctness: 0  | grounded: None  | abstained: True  | citations valid: False (invalid: [])
- judge reason: Assistant abstained although the answer is in the documents.
- gold: [('apply_SIN.pdf', 2)]

## q09 (direct): Who is allowed to give paid immigration advice in Canada?

**Answer:** Only members in good standing of one of the following are allowed to give paid immigration advice in Canada: a Canadian provincial or territorial law society, the Chambre des notaires du Québec, or the College of Immigration and Citizenship Consultants. As of November 23, 2021, the College of Immigration and Citizenship Consultants is the official regulator of immigration and citizenship consultants, and Immigration, Refugees and Citizenship Canada (IRCC) will not accept applications submitted by unlicensed consultants [3247-b-factsheet-do-it-right-eng.pdf, page 1].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The answer correctly identifies the authorized groups for providing paid immigration advice in Canada and is fully supported by the retrieved context.
- gold: [('3247-b-factsheet-do-it-right-eng.pdf', 1)]

## q10 (direct): What can happen to me if I use an unlicensed immigration consultant?

**Answer:** Using an unlicensed immigration consultant can lead to serious consequences, including:

- Losing your money by paying for a service you never received or for fraudulent services.
- Having your application denied if the consultant advises you to apply for a program you’re not eligible for.
- Being barred from entering Canada if the consultant instructs you to lie or hide information on your application, resulting in a 5-year ban.
- Risks of identity theft, money stolen from your bank account or credit card, threats of violence, and exploitation [3247-a-factsheet-unlicensed-consultant-eng.pdf, page 1].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The assistant's answer is correct and complete according to the REFERENCE and all factual claims are supported by the RETRIEVED CONTEXT.
- gold: [('3247-a-factsheet-unlicensed-consultant-eng.pdf', 1)]

## q11 (direct): Will IRCC ever phone me to collect fees or fines?

**Answer:** IRCC will never ask for financial information over the phone, nor will they ask you to pay fees using prepaid credit cards, Western Union, Money Gram, gift cards, or similar services [fraud_newcomers.pdf, page 1].

- correctness: 1  | grounded: False  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The answer correctly states that IRCC will not ask for financial information over the phone, but it does not directly address whether IRCC will phone to collect fees or fines. The grounding is false because the retrieved context does not support the claims made in the answer.
- gold: [('fraud_newcomers.pdf', 1)]

## q12 (direct): On what day of the month is the Canada Child Benefit usually paid?

**Answer:** The Canada Child Benefit is generally paid on the 20th of each month [ccb-2025.pdf, page 9].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The answer correctly states that the Canada Child Benefit is generally paid on the 20th of each month, which is supported by the retrieved context.
- gold: [('ccb-2025.pdf', 9)]

## q13 (direct): By when do I have to tell the CRA that my marital status has changed?

**Answer:** You must inform the CRA by the end of the month following the month in which your marital status changed [ccb-2025.pdf, page 13].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The answer correctly states the requirement to inform the CRA by the end of the month following the change in marital status, which is supported by the retrieved context.
- gold: [('ccb-2025.pdf', 13)]

## q14 (direct): What is the deadline for filing my income tax return in Canada?

**Answer:** The deadline for completing your tax return is April 30 of each year [welcome.pdf, page 108].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The answer correctly states the deadline for filing a tax return in Canada as April 30, which is supported by the retrieved context from page 108 of the document.
- gold: [('welcome.pdf', 108)]

## q15 (direct): What rights will I have if I become a Canadian citizen?

**Answer:** If you become a Canadian citizen, you will have the right to: 
- vote in federal, provincial or territorial, and municipal elections;
- be a candidate in elections; and
- apply for a Canadian passport and enter and leave the country freely [welcome.pdf, page 37].

- correctness: 1  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The assistant answer correctly lists the rights of Canadian citizens as per the retrieved context, but it omits the duty to serve on a jury and the civic responsibility to vote.
- gold: [('welcome.pdf', 37)]

## q16 (direct): Is it legal to drive in Canada without car insurance?

**Answer:** It is strictly illegal to drive without car insurance in Canada [welcome.pdf, page 124].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The answer correctly states that it is illegal to drive without car insurance in Canada, which is supported by the retrieved context.
- gold: [('welcome.pdf', 124)]

## q17 (direct): How many benchmarks does the Canadian Language Benchmarks scale have?

**Answer:** The Canadian Language Benchmarks scale has 12 benchmarks [language-benchmarks.pdf, page 11].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The answer correctly states that the Canadian Language Benchmarks scale has 12 benchmarks, which is supported by the retrieved context from page 11.
- gold: [('language-benchmarks.pdf', 11), ('language-benchmarks.pdf', 16)]

## q18 (direct): Can a permanent resident work for any employer in Canada?

**Answer:** Yes, all permanent residents can work for any employer they wish in Canada [employer-roadmap-en.pdf, page 6].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The answer correctly states that permanent residents can work for any employer in Canada, which is supported by the retrieved context.
- gold: [('employer-roadmap-en.pdf', 6)]

## q19 (direct): Why do privacy commissioners say retailers do not need to record a customer's driver's licence number?

**Answer:** Privacy commissioners say retailers do not need to record a customer's driver's licence number because most business needs can be met by simply examining the identification. They concluded that writing down the driver's licence number or reproducing the card itself cannot be justified, as the number may encode personal information such as the licensee’s birth date, and the card contains a photograph, signature, and other personal information that exceeds what is needed for most business purposes [licence-guide-for-retailers.pdf, page 5].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The assistant's answer is correct and complete according to the REFERENCE and all factual claims are supported by the RETRIEVED CONTEXT.
- gold: [('licence-guide-for-retailers.pdf', 5)]

## q20 (direct): Who can apply for an open work permit because of abuse at work?

**Answer:** Temporary foreign workers in Canada who hold a valid work permit that is employer-specific or was issued under the Seasonal Agricultural Worker Program, or who have applied to renew this type of permit, and who are being abused or at risk of being abused in relation to their job in Canada can apply for an open work permit for vulnerable workers. Family members in Canada can also apply if the principal applicant has been issued an open work permit for vulnerable workers [open-work-permit.pdf, page 1].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The assistant's answer correctly identifies who can apply for an open work permit due to abuse at work and is fully supported by the retrieved context.
- gold: [('open-work-permit.pdf', 1)]

## q21 (multi): What documents do I need to apply for a Social Insurance Number?

**Answer:** To apply for a Social Insurance Number (SIN), you must provide a valid original primary document to prove your identity and legal status in Canada. If the name on your primary document is not the name you are currently using, you may also need to provide a valid supporting document. If you are applying for someone else, additional documents may be required. Importantly, all documents must be valid originals; photocopies are not accepted [apply_SIN.pdf, page 1].

- correctness: 0  | grounded: False  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The answer does not specify the exact documents needed for different statuses (Canadian citizens, permanent residents, temporary residents) as detailed in the REFERENCE.
- gold: [('apply_SIN.pdf', 2), ('apply_SIN.pdf', 3), ('welcome.pdf', 47), ('welcome.pdf', 48)]

## q22 (multi): How can I protect myself from fraud and scams as a newcomer?

**Answer:** To protect yourself from fraud and scams as a newcomer to Canada, you should follow these guidelines:

1. Be cautious of phone calls from people posing as government officials. Remember that Immigration, Refugees and Citizenship Canada (IRCC) will never contact you over the telephone to collect fees or fines, threaten you, or ask for personal or financial information over the phone [fraud_newcomers.pdf, page 1].

2. If you receive a suspicious call, ask for the caller's name, hang up, and verify the call by contacting the IRCC directly. Report any suspicious calls to the Canadian Anti-Fraud Centre or your local police if you have lost money [fraud_newcomers.pdf, page 1].

3. Protect your Personal Identification Number (PIN) for debit and credit cards by never sharing it with anyone, keeping your card safe, and memorizing your PIN. Avoid using obvious information for your PIN and check your account statements regularly [welcome.pdf, page 113].

4. Be wary of telemarketing calls and never provide personal or financial information over the phone unless you initiated the call. If uncertain about a caller, hang up [welcome.pdf, page 114].

5. Be cautious with emails asking for personal information, as they may be phishing attempts. Legitimate companies will not ask for sensitive information via email [welcome.pdf, page 114].

6. Protect your Social Insurance Number (SIN) by not carrying your SIN card, only providing it when legally required, and shredding any documents containing your SIN when no longer needed [protect_SIN.pdf, page 1].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The answer is correct and complete according to the REFERENCE and all factual claims are supported by the RETRIEVED CONTEXT.
- gold: [('fraud_newcomers.pdf', 1), ('fraud_newcomers.pdf', 2), ('protect_SIN.pdf', 1), ('3247-a-factsheet-unlicensed-consultant-eng.pdf', 1)]

## q23 (multi): When should I give out my SIN and when can I refuse?

**Answer:** You should provide your SIN when it is legally required, such as to show to your new employer after finding a job, for income tax purposes, to financial institutions where you earn interest or income, or when applying for certain government benefits like the Canada Pension Plan or Employment Insurance [welcome.pdf, page 48]. 

You can refuse to provide your SIN in situations where it is not legally required, such as when applying for a job, renting a property, negotiating a lease, applying for a credit card, cashing a cheque, or signing up for services like cell phone or Internet [protect_SIN.pdf, page 3]. If asked for your SIN when it is not legally required, you should ask why it is being requested and explain that you do not want to provide it [protect_SIN.pdf, page 3].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The assistant's answer correctly identifies when to provide and refuse a SIN, and all claims are supported by the retrieved context.
- gold: [('protect_SIN.pdf', 2), ('protect_SIN.pdf', 3), ('welcome.pdf', 110)]

## q24 (multi): Who can I trust to help with my immigration application, and who should I avoid?

**Answer:** You can trust a licensed representative who is authorized by the College of Immigration and Citizenship Consultants. It is advisable to ask people you trust for recommendations, get advice from several sources, and check the representative's training and experience. Ensure that you have a written contract that clearly lists the services and fees before signing it. 

You should avoid unlicensed consultants, as they may not have the necessary training or ethical standards, and using them can lead to serious consequences such as losing money, having your application denied, or being barred from entering Canada [3247-a-factsheet-unlicensed-consultant-eng.pdf, page 1][3247-b-factsheet-do-it-right-eng.pdf, page 1].

- correctness: 2  | grounded: True  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The answer correctly identifies licensed representatives as trustworthy and warns against unlicensed consultants, supported by the retrieved context.
- gold: [('3247-a-factsheet-unlicensed-consultant-eng.pdf', 1), ('3247-b-factsheet-do-it-right-eng.pdf', 1)]

## q25 (multi): What health coverage will I have as a newcomer and what does the Canada Health Act require of provincial plans?

**Answer:** As a newcomer, you will be eligible for health coverage under the provincial health care insurance plan if you meet the residency requirements. The Canada Health Act ensures that all bona fide residents of provinces are entitled to coverage under one of the twelve provincial/territorial health care insurance plans. However, you must register for coverage and maintain your eligibility by remaining in your home province or territory for a prescribed number of days each year [canada-health-act-2025.pdf, page 21]. 

The provincial plans must operate in a manner that does not deny coverage or preclude access to necessary hospital and physician services for bona fide residents. Additionally, while provinces can levy taxes and potentially charge premiums, administrative arrangements should ensure that residents are not denied coverage due to an inability to pay premiums [canada-health-act-2025.pdf, page 315].

- correctness: 0  | grounded: False  | abstained: False  | citations valid: True (invalid: [])
- judge reason: The answer does not address the specific health coverage for newcomers or the requirements of the Canada Health Act as outlined in the REFERENCE. It also includes claims not supported by the RETRIEVED CONTEXT.
- gold: [('welcome.pdf', 49), ('welcome.pdf', 50), ('canada-health-act-2025.pdf', 15)]

## q26 (unanswerable): What is the minimum Express Entry CRS score needed to get an invitation?

**Answer:** I don't know based on the provided documents.

- correctness: None  | grounded: None  | abstained: True  | citations valid: False (invalid: [])
- judge reason: Correct abstention.
- gold: []

## q27 (unanswerable): How much does it cost to apply for Canadian citizenship?

**Answer:** I don't know based on the provided documents.

- correctness: None  | grounded: None  | abstained: True  | citations valid: False (invalid: [])
- judge reason: Correct abstention.
- gold: []

## q28 (unanswerable): What is the current minimum wage in Ontario?

**Answer:** I don't know based on the provided documents.

- correctness: None  | grounded: None  | abstained: True  | citations valid: False (invalid: [])
- judge reason: Correct abstention.
- gold: []

## q29 (unanswerable): Who won the hockey game last night?

**Answer:** I don't know based on the provided documents.

- correctness: None  | grounded: None  | abstained: True  | citations valid: False (invalid: [])
- judge reason: Correct abstention.
- gold: []

## q30 (unanswerable): What is the best mortgage interest rate available right now?

**Answer:** I don't know based on the provided documents.

- correctness: None  | grounded: None  | abstained: True  | citations valid: False (invalid: [])
- judge reason: Correct abstention.
- gold: []
