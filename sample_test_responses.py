'''
Sample test set just to make sure the RAG is not completely a dud

Question 1:- What is the monthly cost of the Fiber 500 plan?
Response:- 'output': 'I don’t have the Fiber 500 monthly price in the provided knowledge base. 
The materials reference that monthly pricing must be shown (Broadband Label) but do not list the current amount.\n\n
For the exact, up-to-date monthly cost and any available promotions, please call Customer Support at 1-800-1212-9090.
\n\nNotes from the KB that may be relevant:\n- Standard installation fee is $99, waived for customers signing a 24-month commitment or 
migrating from legacy DSL.\n- Promotional discounts and bundling credits may affect the effective monthly price.
\n- For month-to-month plans, price changes require a minimum 60 days’ notice.'

Conclusion - Right Response


Question 2:- Wht are some residential home internet installation pre-requisites?
Response:- [{'output': 'Here are the residential installation pre-requisites per the Residential Fiber & Fixed-Line Installation Standards:
 Power outlet: A dedicated, grounded 120V AC power outlet must be available within 1.5 meters (5 feet) of the planned Optical Network Terminal (ONT)
or Gateway placement.\n- Demarcation Point access: Access to the Demarcation Point (the external entry point where the provider’s 
network meets the home) must be unobstructed. The technician will identify this point.\n- Structural permissions (rental properties): 
For drill-through entry (the creation of a 1/2-inch hole for fiber/coaxial cable entry), written landlord consent is required
General access/path: Ensure a clear, accessible path from the Demarc Point to the interior location where the ONT/Gateway will be placed, 
allowing for cable routing without obstructions.\n\nThese prerequisites should be arranged before the technician is dispatched to avoid 
installation delays. If you need further guidance, you may contact Customer Support.'}]

Conclusion - Right Response


Question 3 - Can you explain notice period for price increases?
Response - 'output': 'Here is how notice periods for price changes work:\n\n- Month-to-month plans:
At least 60 days written notice prior to any rate adjustment.\n- Fixed-term contracts (e.g., 2-year deals):
The price cannot be increased during the term unless the change results in a cost reduction or a speed increase for the same price 
  i.e., a benefit must accompany any price change).\n- Promotions and bundling: Discounts and credits can affect the effective monthly price,
so the visible price may differ from the base rate.
For exact details on your specific plan and any current promotions, please contact Customer Support at 1-800-1212-9090.

Conclusion - Right Response


Final conclusion - Good enough for the purposes of red teaming.

'''