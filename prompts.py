
finance_expert = """

You are a finance expert with an in-depth understanding of monetary management and investment, encompassing financial analysis, risk assessment, and strategic financial planning. Your analytical skills enable you to decode intricate financial data, facilitating well-informed decisions for economic success.

Currently, you are analyzing the Q4 2023 Earnings Conference Call from Celestica Inc. (NYSE:CLS). User queries will be presented within **** characters, and your responses should be based solely on the extracts enclosed by #### characters.

The conference call addresses forward-looking statements in accordance with the U.S. Private Securities Litigation Reform Act of 1995 and relevant Canadian securities laws. These statements rely on management's expectations, subject to potential risks, uncertainties, and other factors that may differ from expressed conclusions, forecasts, or projections.

Additionally, the call mentions various non-IFRS financial measures, such as non-IFRS operating margin, adjusted gross margin, adjusted ROIC, adjusted free cash flow, gross debt to non-IFRS trailing 12-month adjusted EBITDA leverage ratio, adjusted EPS, adjusted SG&A expense, adjusted effective tax rate, and operating earnings.

**Rules:**

1. Only respond to questions answerable with the provided extracts.
2. Each extract contains a reference ID enclosed by <> characters. For every extract used in formulating your answer, append the reference ID at the end of the response.
3. Keep your responses concise.
4. Format your answers in markdown.

"""

multiple_answers = """

You are a finance expert with an in-depth understanding of monetary management and investment, encompassing financial analysis, risk assessment, and strategic financial planning. Your analytical skills enable you to decode intricate financial data, facilitating well-informed decisions for economic success.

Currently, you are analyzing the Q4 2023 Earnings Conference Call from Celestica Inc. (NYSE:CLS), this document is enclosed by #### characters. Based on the conference call, your task is to output three possible answers for the user's query enclosed by **** characters.

The conference call addresses forward-looking statements in accordance with the U.S. Private Securities Litigation Reform Act of 1995 and relevant Canadian securities laws. These statements rely on management's expectations, subject to potential risks, uncertainties, and other factors that may differ from expressed conclusions, forecasts, or projections.

Additionally, the call mentions various non-IFRS financial measures, such as non-IFRS operating margin, adjusted gross margin, adjusted ROIC, adjusted free cash flow, gross debt to non-IFRS trailing 12-month adjusted EBITDA leverage ratio, adjusted EPS, adjusted SG&A expense, adjusted effective tax rate, and operating earnings.

**Rules:**

1. Only respond to questions answerable with the provided extracts.
3. Keep your responses concise.
4. Output 3 possible answers, each answer should be delimited by ==== characters.
5. Format your answers in markdown.


"""

doc = """

##################
Celestica Inc. (NYSE:CLS) Q4 2023 Earnings Conference Call January 30, 2024 8:00 AM ET

Company Participants:

Craig Oberg - VP, IR & Corporate Development
Rob Mionis - President & CEO
Mandeep Chawla - CFO

Conference Call Participants:

Robert Young - Canaccord
Maxim Matushansky - RBC Capital Markets
Thanos Moschopoulos - BMO
Daniel Chan - TD Securities
Matt Sheerin - Stifel
Todd Coupland - CIBC
#####################
----
Presentation

Operator
Good day, ladies and gentlemen, and welcome to Celestica Q4 2023 Earnings Conference Call. At this time, all lines are in a listen-only mode. Following the presentation, we will conduct a question-and-answer session. [Operator Instructions] This call is being recorded on Tuesday, January 30, 2024.
I would now like to turn the conference over to Craig Oberg, Vice President of Investor Relations and Corporate Development. Please go ahead.

Craig Oberg - VP, IR & Corporate Development
Good morning and thank you for joining us on Celestica’s fourth quarter 2023 earnings conference call. On the call today are Rob Mionis, President and Chief Executive Officer; and Mandeep Chawla, Chief Financial Officer.
As a reminder, during this call, we will make forward-looking statements within the meanings of the U.S. Private Securities Litigation Reform Act of 1995 and applicable Canadian securities laws. Such forward-looking statements are based on management’s current expectations, forecasts and assumptions which are subject to risks, uncertainties and other factors that could cause actual outcomes and results to differ materially from conclusions, forecasts or projections expressed in such statements.
For identification and discussion of such factors and assumptions, as well as further information concerning forward-looking statements, please refer to yesterday’s press release, including the cautionary note regarding forward-looking statements therein, our most recent annual report on Form 20-F and our other public filings, which can be accessed at sec.gov and sedarplus.com. We assume no obligation to update any forward-looking statement, except as required by law.
In addition, during this call, we will refer to various non-IFRS financial measures, including ratios based on non-IFRS financial measures consisting of non-IFRS operating margin, adjusted gross margin, adjusted return on invested capital or adjusted ROIC, adjusted free cash flow, gross debt to non-IFRS trailing 12-month adjusted EBITDA leverage ratio, adjusted earnings per share or adjusted EPS, adjusted SG&A expense, adjusted effective tax rate and operating earnings.
Listeners should be cautioned that references to any of the foregoing measures during this call denote non-IFRS financial measures whether or not specifically designated as such. These non-IFRS financial measures do not have any standardized meanings prescribed by IFRS and may not be comparable to similar measures presented by other public companies that report under IFRS or who report under U.S. GAAP and use non-GAAP financial measures to describe similar operating metrics.
We refer you to yesterday’s press release and our Q4 2023 earnings presentation, which are available at celestica.com under the Investor Relations tab, for more information about these and certain other non-IFRS financial measures, including a reconciliation of historical non-IFRS financial measures to the most directly comparable IFRS financial measures from our financial statements and a description of recent modifications to specified non-IFRS financial measures. Unless otherwise specified, all references to dollars on this call are to U.S. dollars and per share information is based on diluted shares outstanding.
Let me now turn the call over to Rob.

Rob Mionis - President & CEO
Thank you, Craig. Good morning, everyone, and thank you for joining us on today's call. We ended the year with a very strong fourth quarter, achieving revenue of $2.14 billion, which is towards the high-end of our guidance range, while our non-IFRS adjusted EPS came in at $0.76, exceeding the high end of our guidance range. Our non-IFRS operating margin was 6% exceeding the midpoint of our revenue and non-IFRS adjusted EPS guidance ranges.
The outperformance in the fourth quarter relative to our guidance was driven by continued strength in our CCS segment, supported by the sustained growth of our hyperscaler portfolio. We continue to see the benefit of improved mix in our CCS segment margin, which reached yet another new high of 6.7% in the fourth quarter.
In our ATS segment, revenues were down slightly year-to-year as incremental demand softness in our industrial business and continued demand headwinds in our capital equipment business more than offset strong growth in our A&D business. Our solid performance in the fourth quarter capped a stellar year in 2023. Throughout this past year, we continued to execute on our strategic firm, enhanced our competitive presence in key markets and consistently delivered on our financial objectives.
In 2023, our business generated revenue of approximately $8 billion, 10% higher than 2022, driven by strong growth in both our CCS and ATS segments. Our non-IFRS adjusted EPS of $2.43 was up 28% versus the prior year, while non-IFRS operating margin of 5.6% was higher by 70 basis points, with both results marking the highest in the company's history. Our strong profitability and working capital management allowed us to generate non-IFRS adjusted free cash flow of $194 million, exceeding our full year target of $150 million.
Before I provide an update on the market outlook for each of our businesses, I would now like to turn the call over to Mandeep, who will provide further details on our fourth quarter financial performance and our guidance for the first quarter of 2024.
Mandeep, over to you.

Mandeep Chawla - CFO
Thank you, Rob, and good morning, everyone. Fourth quarter revenue came in at $2.14 billion, towards the high end of our guidance range. Revenue was up 5% year-over-year, supported by solid growth in our CCS segment, partially offset by a modest decline in our ATS segment.
Our fourth quarter non-IFRS operating margin of 6.0% was 70 basis points higher year-over-year and marked the highest quarterly results in the company's history. Our margin expansion was driven primarily by higher profitability in both segments, as a result of improved mix, production efficiencies, and higher volumes in our CCS segment.
Non-IFRS adjusted earnings per share for the fourth quarter was $0.76 exceeding the high end of our guidance range. This result was $0.20 higher year-over-year, driven primarily by higher non-IFRS operating earnings, as well as lower interest costs, a more favorable non-IFRS adjusted effective tax rate and lower shares outstanding.
Moving onto our segment performance. ATS revenues in the fourth quarter were $803 million down 2% year-over-year, slightly below our expectations of a low-single digit percentage increase. The year-over-year decline in ATS segment revenue was driven by demand softness in our industrial business, primarily as a result of slowing demand in certain programs, as well as continued demand headwinds in our capital equipment business.
These declines were partially offset by solid performance in our A&D business, which saw growth of more than 20% compared to the prior year period. ATS segment revenues accounted 38% of total revenues in the fourth quarter compared to 40% in the same period last year.
Our fourth quarter CCS segment revenue of $1.34 billion was up 10% compared to the prior year period, driven by very strong growth in our enterprise end market, partially offset by anticipated demand softness in our communications end market. CCS segment revenue accounted for 62% of total company revenues in the quarter compared to 60% in the prior year period.
Enterprise end market revenue in the fourth quarter was up 46% year-over-year, meaningfully above our expectation of a high-20s percentage increase. This growth was driven by ramping programs and strengthening demand for AI/ML compute from our hyperscaler customers. Revenue in our communications end market was lower by 10% compared to the prior year period, better than our expectation of a mid-teens percentage decrease.
Similar to last quarter, the decline was driven primarily by tough comps, as some of our customers continue to digest inventory purchased in the prior year. HPS revenue was $484 million in the quarter, 1% lower year-over-year. HPS revenues were 23% of total company revenues in the fourth quarter compared to 24% in the prior year period.
Turning to segment margins. ATS segment margin in the fourth quarter was 4.7%, up 30 basis points year-over-year, driven by strong productivity and favorable mix. CCS segment margin during the quarter was 6.7%, up 80 basis points year-over-year, driven by higher volumes and improved mix, including significant growth with our hyperscaler customers.
During the fourth quarter and for 2023, we had one customer, which accounted for more than 10% of total revenues, representing 29% for the quarter and 22% for the year. Celestica has a long standing relationship with this customer, a global hyperscaler that we have been supporting for well over a decade. We support this customer across 25 programs covering HPS and non-HPS products in the areas of networking and compute.
The products we build are highly complex, and as a result, the majority of these programs are single sourced. In addition, we are pleased that as a result of our strength in engineering and solid operational execution, we continue to win new programs with this customer and expect to see demand strength continue through 2024 and into 2025.
Moving onto some additional financial metrics. IFRS net earnings for the fourth quarter were $84 million or $0.70 per share compared to net earnings of $42 million or $0.35 per share in the prior year period. Adjusted gross margin for the fourth quarter was 10.4% up 100 basis points year-over-year, due to improved mix and production efficiencies.
Fourth quarter non-IFRS adjusted effective tax rate was 20% in the quarter compared to 23% in the prior year period. Non-IFRS adjusted ROIC for the fourth quarter was 23.3%, an improvement of 2.6% compared to the prior year quarter driven by strong profitability and working capital managements.
Moving on to working capital. At the end of the fourth quarter, our inventory balance was $2.11 billion, down $155 million sequentially, and down $244 million year-over-year. Cash deposits were at $905 million at the end of the fourth quarter, up $30 million sequentially, and higher by $79 million compared to the prior year period.
When accounting for cash deposits, inventory at the end of the fourth quarter was lower by $323 million on a year-over-year basis and lower by $185 million sequentially. Inventory days, net of cash deposit days were 62 in the fourth quarter compared to 79 in the prior year period. We are pleased with the improvements we are seeing in inventory as material constraints continue to improve and [indiscernible] lead times normalize. Cash cycle days were 72 during the fourth quarter, flat sequentially, and 8 days higher than the prior year period.
Capital expenditures for the quarter were $33 million or approximately 1.5% of revenue, compared with 1.6% of revenue in the fourth quarter of 2022. For the full year, capital expenditures were $125 million or 1.6% of revenue as we continue to invest in growth across our network to support customer demand.
As we look to 2024, we expect our capital expenditures to modestly increase to between 1.75% and 2.25% of revenues, with a higher level of spend in the first half of the year. Our increasing level of capital expenditures is geared towards capacity expansions at key sites in support of demand for AI/ML compute and HPS programs.
In Thailand, we are currently building out over 100,000 square feet of additional capacity, with the first phase expected to be online in the first quarter of 2024, and the second phase expected to be completed in the first half of 2025. This expansion is being partially funded by a co-investment with one of our hyperscaler customers to facilitate demand for highly specialized data center products.
And in Malaysia, we are building more than 80,000 square feet of capacity to support strong demand from customers in our CCS segment, including our HPS business. This edition is expected to be online in the first half of 2024.
Turning to non-IFRS adjusted free cash flow. We generated $84 million in the fourth quarter compared to $43 million in the prior year period, marking our 20th consecutive quarter of positive non-IFRS adjusted free cash flow. This result brings our total free cash flow for the year to $194 million ahead of our full year outlook of $150 million and approximately double our results from 2022 of $94 million. The out performance was driven by strong profitability and working capital management.
Looking forward to 2024, we are expecting $200 million or more of non-IFRS adjusted free cash flow, $25 million higher than the outlook we shared in our November Virtual Investor meeting.
Moving on to some additional key metrics. At the end of the fourth quarter, our cash balance was $370 million, higher by $17 million sequentially. In combination with our approximately $600 million of borrowing capacity under our revolver, this provides us with liquidity of approximately $1 billion, which we believe is sufficient to meet our anticipated business needs.
Our gross debt at the end of the fourth quarter was $609 million, leaving us with a net debt position of $239 million. Our fourth quarter gross debt to non-IFRS trailing 12-month adjusted EBITDA leverage ratio was 1.1 turns flat sequentially and down 0.2 turns compared to the same period of last year.
As of December 31, 2023, we were compliant with all financial covenants under our credit agreement. During the fourth quarter, we purchased approximately 400,000 shares for cancellation under our normal course issuer bid at a cost of $10 million. For 2023, we repurchased a total of 2.6 million shares for cancellation, or approximately 2% of our shares outstanding at year end, at a total cost of $36 million.
In December, the TSX accepted our normal course issuer bid, which is in effect until December 2024. Under this new NCIB, we are authorized to purchase up to approximately 11.8 million shares, or approximately 10% of the public flow. We continue to believe that investing in our share buyback program is a good use of capital and intend to repurchase shares on an opportunistic basis in 2024.
Now turning to our guidance for the first quarter of 2024. First quarter revenues are expected to be in the range of $2.025 billion to $2.175 billion, which, if the midpoint of this range is achieved, would represent growth of 14% compared to the prior year period. First quarter non-IFRS adjusted earnings per share are expected to be in the range of $0.67 to $0.77 per share, which at the midpoint would represent an improvement of $0.25 per share or 53% compared to the first quarter of 2023. If the midpoint of our revenue and non-IFRS adjusted EPS guidance ranges are achieved, non-IFRS operating margin would be 6.0%, which would represent an increase of 80 basis points over the same period last year.
Non-IFRS adjusted SG&A expense for the first quarter is expected to be in the range of $62 million to $64 million. We anticipate our non-IFRS adjusted effective tax rate to be approximately 20% for the first quarter, excluding any impact from taxable foreign exchange or unanticipated tax elements. Our first quarter guidance assumes that our income will be subject to global minimum tax, as legislation that has been introduced in Canada may be approved before the end of the quarter. If this legislation is not substantially enacted in the first quarter, our estimate for our first quarter non-IR4S adjusted effective tax rate would be approximately 15%.
Now turning to our end market and outlook for the first quarter of 2024. In our ATS segment, we anticipate revenue to be down in the low-single digit percentage range year-over-year, driven by demand softness in our industrial business and ongoing market softness in capital equipment, partly offset by continued growth in A&D. We anticipate revenues in our communications end market to be up in the low-single digit percentage range year-over-year, driven by strengthening demand and networking from hyperscaler customers, including in our HPS programs.
Finally, in our enterprise end market, we expect revenue to be up in the high-60s percentage range year-over-year, driven by anticipated demand growth in AI/ML compute programs from our hyperscaler customers.
I'll now turn the call back over to Rob to discuss the outlook for each of our end markets and the overall business.

Rob Mionis - President & CEO
Thank you, Mandy. Before discussing the outlook for our markets, I would like to reaffirm the following metrics from our 2024 financial outlook that we provided at our Virtual Investor meeting in November. We continue to expect revenue of $8.5 billion or more, non-IFRS adjusted EPS of $2.70 or more, and non-IFRS operating margin to be in the range of 5.5% to 6%.
In addition, as Mandeep mentioned, we have raised our non-IFRS free cash flow outlook for the year to $200 million or more. We are pleased with our strong performance in 2023 and continue to see very positive momentum in the first quarter of 2024. As such, we are currently undertaking discussions with our customers and suppliers in order to obtain better visibility into the remainder of the year. And we look forward to providing an update on our 2024 outlook with our first quarter results.
Now moving on to the outlook for each of our businesses. Beginning with our ATS segment, our industrial business recorded annual growth of 29% in 2023, driven by ramping programs in smart (ph) energy and EV charging. However, we began to see signs of market softness towards the end of the year, due in part to pockets of weakness in the broader economic environment, higher interest rates, as well as some delays in new program ramps.
As such, we expect to see lower revenues in our industrial portfolio through the first half of the year before seeing a return to year-to-year growth in the second half, which should result in modest growth in our industrial business for all of 2024 when compared to 2023. We continue to believe that the structural trend in markets such as EV charging, smart (ph) energy, and telematics, amongst others, remain intact and are supportive to growth in our industrial business over the long term.
In our A&D business, the sustained recovery in commercial aerospace has seen domestic air travel surpass pre-pandemic levels in many economies, resulting an annual revenue growth of more than 30% in 2023 compared to 2022. Looking ahead, we expect to see strong demand across our commercial aerospace submarkets to continue in 2024.
Our defense business is also expected to see solid growth in the year ahead, supported by new program wins, and increased government investment in military capabilities. Overall, we anticipate the sell demand to drive low-double digit percentage growth in our A&D business in 2024 compared to 2023.
In our capital equipment business, market forecasts continue to suggest that the underlying market demand is operating close to trough levels, and we should see flat to slightly higher demand in 2024. We are maintaining our outlook for modest revenue growth in our capital equipment business in 2024, supported by the ramping of new program wins and our assumption of base demand holding flag for 2023. We anticipate that the year-to-year growth will largely be in the back half of the year, setting up for a stronger recovery and demand in 2025.
In our Health Tech business, we anticipate our revenue to grow in 2024 compared to 2023 as we wrap new programs. So for our overall ATS segment, we currently anticipate that revenue will decline slightly in the first half of 2024 compared to 2023 to the pockets of macro weakness affecting some of our markets. However, we anticipate that segment revenue will resume year-to-year growth in the second half of the year. Overall, we are maintaining our expectation for ATS revenue growth in the mid-single digit percentage range in 2024.
Now turning to our CCS segment. The demand backdrop for our CCS segment continues to be very strong. Investments from hyperscalers and data center infrastructure are fueling significant CapEx spending, driven by growing demand for artificial intelligence and machine learning applications. In 2023, our portfolio with our hyperscalers saw revenue growth of 32% compared to 2022, recording nearly $2.9 billion in revenues. This accounted for 62% of our total CCS segment revenues in 2023, up from 51% the prior year.
At our recent Virtual Investor meeting in November, we delved further into this dynamic, which we believe is long-term and structural in nature. We anticipate this solid growth to continue in 2024 and believe that this investment cycle has the potential to support several years of strong demand for our CCS segment. The demand outlook for our enterprise and market continues to be impressive as the beneficiary of hyperscaler's growing deployment of AI/ML compute capacity.
We're seeing the strong momentum from 2023 continue, and as mentioned earlier, we anticipate significant growth within our AI/ML compute portfolio as we enter 2024. We expect additional growth in our storage business to materialize in the latter half of the year, driven by demand from new programs. After experiencing some softness in 2023, demand in our communications end market is anticipated to resume year-to-year growth in the first quarter, driven by a resumption of strength in networking demand from hyperscalers, which is expected to persist throughout the year.
Within our HPS business, we anticipate to resume year-to-year growth in the first quarter of 2024 and for the full year. This growth is being fueled by a number of new program loans in both networking, supported by growth in our 400G and 800G platforms, and to some extent AI/ML compute. For 2024, we are maintaining our previously communicated expectation of low-double digit percentage revenue growth in our CCS segment, supported by solid growth in both our enterprise and communications end markets.
Although, we are seeing some divergence in the short-term demand dynamics underlying our various end markets, we believe that the fundamentals supporting our overall business are very constructive due to the benefits of our strategic portfolio diversification and our consistent execution. We feel that our positioning for 2024 remains positive, as we remain confident in our ability to meet our financial outlook and improve on our very strong performance in 2023.
With that, I would now like to turn the call over to the operator for questions.

Craig Oberg - VP, IR & Corporate Development
Thank you.
----

++++++++

Q&A Session

Operator
Thank you, sir. Ladies and gentlemen, we will now begin the question-and-answer session. [Operator Instructions] Our first question comes from the line of Robert Young from Canaccord Annuity. Please go ahead.

Robert Young - Canaccord
Hi. Can you give us a little bit of color on the hyperscale business and CCS, given the large customer accounting for 29%, it's a pretty significant chunk. Maybe if you could talk about the business outside of that large customer, is that driven by the high level of AI compute currently, and there's one customer or a small number of customers there, or is there some other dynamic going on there?

Rob Mionis - President & CEO
Well, hi, Rob. So with this particular customer, it's a hyperscale of customer, they're making significant investments in AI/ML compute, as well as networking. As you mentioned on the call, we have over 25 programs with this customer and it's comprised of everything from hardware platform solutions to high value EMS to even services. They're an industry leader. We've been doing business with them for over a decade. And they're also co-investing with us on some CapEx facility investments over in Thailand, so a very healthy relationship. Across the broader hyperscaler business, we're also seeing strong growth from several others in the same area and we expect the concentration to improve over time as ebbs and flows in people's investment cycles.

Mandeep Chawla - CFO
I would just add to that, Rob that, as a reminder, we do business with the top five hyperscalers and while we are doing a lot of AI/ML compute with the large customer that Rob just talked about, we're starting to see some return and demand coming on the networking side, which is helping us across the customer base and we're really encouraged that as we go into the first quarter now, we're seeing growth resume in communications, we're seeing growth resume in hardware platform solutions, and those are offerings that we provide across the customer base.

Robert Young - Canaccord
Okay. Thank you. Yeah. And then the second question, maybe I'm getting ahead of myself. You said you're going to revisit the full year outlook, I think in Q1, but the outlook for 5.5% to 6% operating margin seems conservative given, you're doing so well in the enterprise business in CCS at 6.7% and you're entering at 6% and the guide looks like 6%. So it looks as though it's going to decelerate in the back half of the year. Maybe if you could discuss that and I'll pass on.

Mandeep Chawla - CFO
Yeah, Rob. I'll talk about two things. one is the outlook for the full year and then I can talk to your point on margin specifically. So, when we look at full year 2024, we're really pleased with the way we ended ‘23. And clearly, we're off to a really hot start now into the first quarter. And again, encouraged by where we're seeing the demand signals come through, both on comms and HPS, but also the demand signals from the hyperscalers continue to strengthen.
As you know, in November, we provided the outlook of $8.5 billion or more and $2.70 of EPS or more. And right now, we really do see that as being the floor. What we are looking to do, as Rob mentioned in his prepared remarks is, we're going back out to the customer base and revalidating the second half outlook. We're seeing that increased strength happening in the first half and now what we want to do is go and validate whether or not those increasing level of demand signals are going to be added to the second half as well. And so, in April, we'll come back with an updated forecast.
To your point on the margin profile itself, as we talked about, ATS is expected to see some very minor levels of declines in the first half of this year before resuming growth in the back end of the year. ATS, again, we're expecting across all of our end markets to have some level of growth in 2024. But because that growth in the back half is going to be off the back of ramping programs, there is going to be a little bit of margin challenges around there as well. Again, 6% for the first quarter, I believe the 270 is the floor. And obviously, we're going to be working towards the high end of that 5.5% to 6% range as best we can.

Rob Mionis - President & CEO
And one other thing, I would add, Rob, I think by the end of the first quarter we'll have better visibility into capital equipment markets. We are seeing some signs of recovery. We're cautiously optimistic. Some of our customers are starting to restock consumables and spares, which is a good sign. So I think as capital equipment gets better, so will some of the ATS margins as well.

Robert Young - Canaccord
Okay. Thank you. I'll pass on.

Rob Mionis - President & CEO
Okay.

Operator
Thank you. We have our next question coming from the line of Maxim Matushansky from RBC Capital Markets. Please go ahead.

Maxim Matushansky - RBC Capital Markets
Hi, good morning. Just on the Communications segment, has there been any changes to your expectation for the networking growth to resume in Q1, or is it just the OEM business that's offsetting the hyperscaler strength? I think I see that the guidance implies a core record deceleration. So is that to mean that, that is primarily because of the OEM business softness?

Rob Mionis - President & CEO
No. As we head into Q1, we expect communications and networking to actually be up, driven by a hopper scalers, both on 400G and 800G programs and there's also, HPS driven programs. So, as we head into last year, we had some tough comps. Some of those tough comps are lapsing, and now we're seeing comps return to growth.

Maxim Matushansky - RBC Capital Markets
Got it. And on the hyperscalers, is there any changes from your last update, I guess, in November on your hyperscaler customer programs and your expected demand over the next few quarters? And I know you talked about a new program wins with your largest customer, is that something that you anticipated in previous quarters or is that something that's new?

Rob Mionis - President & CEO
Yeah. We've been on our hyperscaler programs. We've actually been winning incremental share. That on top of increased demand strength has both been positive for us and some of the reasons for some of the improved outlook that we're seeing into Q1 and potentially for the full year, hence, that's why we're going to take a quarter to revisit with our customers and take a look at what the full year has to be. But we have been winning some incremental share and been booking a really significant amount of 800G programs.

Maxim Matushansky - RBC Capital Markets
And just finally for me. Just to revisit, ATS, I think some of your peers have also been seeing a slowdown in their end markets over the last little bit based on customers working through their inventory buffers. Is that what you're seeing as well this quarter and can you maybe speak to within industrial and capital equipment end markets specifically, and what is causing you to expect demand to return by the second half? Is it primarily kind of those new program ramps?

Rob Mionis - President & CEO
Yeah. Good question. So our industrial business in ‘23, a way of reminder, grew close to 30%. Again, it was fueled by green energy programs, including EV charging, energy storage, energy generation. As we were exiting the year, demand started cycling down in some of these markets and the markets that were really impacted were interest rate sensitive markets, but moreover, because the material environment has dramatically improved, our customers were taking the opportunity to reduce their strategic inventory buffers. We think those buffers will normalize in the first half of the year, and in the second half of the year, we have new programs, ramps planned, which would return the industrial business to growth.
And our capital equipment business, as I mentioned earlier, we're cautiously optimistic as we get to the back half of the year and certainly into 2025 that we're seeing some signs of growth and the costs are pretty much aligned there. And again, we're seeing some spares orders. And as a reminder, some of the headwinds that we're seeing in ATS we think will be more than offset with our strength that we're seeing in our CCS business.

Maxim Matushansky - RBC Capital Markets
Great. Thanks. I'll pass the line.

Operator
Thank you. We have our next question coming from the line of Thanos Moschopoulos from BMO Capital Markets. Please go ahead.

Thanos Moschopoulos - BMO
Hi. Good morning. With respect to the full year guidance, I hear you with respect to wanting to discuss the second half outlook with your customers before revisiting the guidance. But certainly from the demand signals, you're highlighting it seems like it'll be a stronger second half. I guess from your perspective, what might be the key areas of uncertainty you want to further color on before visiting guidance? Would that be on semi and industrial, or which areas would be the biggest source of demand variability as you think about second half?

Mandeep Chawla - CFO
Yeah. Hi, Thanos. Mandeep here. So we were pleased to be able to interlock with our customer base, specifically on the hyperscaler side in the fourth quarter, and that has led us to confidently come out with the outlook that we did. Even after our virtual investor meeting in November, we saw incremental improvement to the forecast coming from the hyperscalers, and so that's reflected in our Q1 guidance.
Again, our outlook is for 14% year-over-year growth, which is higher than what we would have said probably in November. And we're seeing that demand strength continue into the second quarter. So the conversations with the hyperscalers are, is there an improvement in material availability on your end? Is there -- has your deployment change -- plans changed at all? And how does that impact the second half of the year? Is it going to be similar to what we're seeing right now in the first half of the year?
And then to Rob's point on capital equipment. So our assumption right now is that the base market is going to be flat. We're around trough levels right now, some encouraging signs as Rob talked about, and where we're expecting the growth to be in capital equipment is as we ramp AS/ML. AS/ML is a customer of ours for a few years now, but we've won a number of programs over the last year or so, and those programs are in the process of being ramped right now, and the demand signals from that specific customer have not changed.
And so what we're looking to do as we go to the rest of the customer base in capital equipment is to understand whether or not some of these early signs that we're seeing in terms of consumables and spares is going to lead to a demand uptick in the back end of the year. And so it's really around hyperscalers and capital equipment.

Thanos Moschopoulos - BMO
That's helpful. And then on the softness in industrial, just to clarify, is that primarily lead edged in green energy or is that kind of across the board in your various end markets of an industrial?

Rob Mionis - President & CEO
I thought also its pronounced mostly in EV charging, which is kind of being driven by a slowdown in EV sales and also some of the incentives, at least in the U.S. are slow to get out to the marketplace, that's having some impact as well as the higher interest rates. But we're also seeing a little bit of a slowdown in, I'll call it the broader industrial space, just driven by the burn down of strategic inventory buffers. Again, we expect some new program ramps and the burn down of the buffers for this entire industrial business to start resuming to grow from the back half of the year.

Thanos Moschopoulos - BMO
Great. [indiscernible]

Rob Mionis - President & CEO
Thanks.

Operator
Thank you. We have our next question coming from the line of Daniel Chan from TD Securities. Please go ahead.

Daniel Chan - TD Securities
Hi. Good morning. Congrats on a strong quarter here. So communications was stronger than expected this quarter, was that driven by AI demand strength or was that from non-AI related cloud demand where we're also starting to see some early signs of recovery?

Rob Mionis - President & CEO
In terms of comms, it was driven by networking, which is kind of the pull through that we've been mentioning that we would see as a result of AI/ML demand. And within networking, there's, I'll call it, AI/ML networking, which is directly driven and we've seen both in those programs, networking comes in a couple different flavors. The 48 volt is really driven by some of the AI/ML applications and we've certainly seen an uptick in that.

Daniel Chan - TD Securities
And then, we've seen a lot of new data center leasing activity. So just curious on the timing of this communications ramp as you guys are expecting 800G to ramp into 2025. So with all these new data centers coming online, are these new builds going to have 800G in them or will they leverage 400G to begin with? So just wondering, like, with them building out all these new data centers this year, whether they're going to be putting a lot of that next generation stuff or whether they're going with current generation equipment.

Rob Mionis - President & CEO
That's a good question. What I can tell you is that 400G is strong throughout the year. 800G is starting to ramp in the first half of the year, very strong in the back half of the year and certainly picking up into ‘25. That would lead me to believe it's a little bit of a blend, but to be frank with you, I'm not entirely sure.

Mandeep Chawla - CFO
One of the things that we are seeing, Dan, is that within some of our customers' CapEx spending, they are shifting CapEx towards AI applications, and so making a decision to refresh certain data centers over other data centers. In addition to that, what we're also seeing is that for some of the customers, as silicon becomes available, they're looking for 400G solutions while they wait for 800G to be available in 2025 as it goes through the design cycle, etc. So we are seeing a shift of investment towards AI applications, and sometimes that's at the expense of more traditional cloud applications.

Daniel Chan - TD Securities
Appreciate it. Thanks for that. And the final question, you also mentioned the ramp up of some of these sites. Just wondering whether you have enough capacity to deal with the near-term demand that's coming in throughout this year and how those discussions are going on your ability to service some of that demand? Thank you.

Rob Mionis - President & CEO
Yeah. Thanks. We've been interlocking with our customers and been investing forward on capacity expansions, mainly in Thailand. We have a couple of phases, and also in Malaysia, a phase is coming online in February, we've been cutting, frankly. So yes, we do have enough capacity, and it's coming online, very much aligned with the demand state, I would say. And these are also highly automated factories, highly automated test centers, so they're really producing a lot of productivity.

Daniel Chan - TD Securities
Great. Thanks.

Operator
Thank you. We have our next question coming from the line of Matt Sheerin from Stiefel. Please go ahead.

Matt Sheerin - Stifel
Yes. Thank you. Good morning. My first question just wanted to go circle back to the guidance for CCS and understanding sort of lack of visibility into the back half. But just looking at Q2, I know you have some visibility. Obviously, you're going to be up in enterprise high-60s year-over-year. And I know there's a lot of lumpiness in that business where you're up double-digits one quarter and then there's a digestion period. So what should we think about, Mandeep, in terms of modeling at least sort of the first half into Q3 in terms of seasonality and obviously there's not a lot of seasonality, it's different, but how should we think about that, the cadence there?

Mandeep Chawla - CFO
Yeah. Good morning Matt. So we do have from our legacy OEM accounts a little bit of seasonality in our first quarter. And as such, I think you can think about the first quarter revenue number being the low point for the year. We are looking for sequential improvement as we go into the second quarter. And then again, just wanted to maybe clarify some of the wording, which is, we do have an interlock with our customer base in the back half of the year. And that interlock gives us the confidence to be able to say the outlook that we're getting, which is right now we believe the 8.5 billion should be the floor.
What we have seen though is that after the interlocks, requests from customers to say, can you give me actually more product and can you give it to me sooner than what I had originally asked for? And so that's what's filling in right now Q1 and Q2. And so the conversations with the customers are around have you changed your outlook for the back half of the year and what is driving that? Is it because you're accelerating data center deployments? Is it because there is a better level of availability (ph) which is happening? And then how does that impact the last two quarters the way it's impacting the first two quarters? So positive conversations for sure. And we do have a level of visibility is to really see if we can increase the numbers or not.

Matt Sheerin - Stifel
And so based on that, would you expect the Q2 to be up sequentially then again?

Mandeep Chawla - CFO
On a revenue basis, yes.

Matt Sheerin - Stifel
What's that?

Mandeep Chawla - CFO
Yes. We would expect higher revenues in Q2 than we do in Q1.

Matt Sheerin - Stifel
Pro CCS, okay. Perfect. And then the capacity adds in Thailand and Malaysia. Rob, could you give us a ballpark in terms of the revenue production capacity in each of those or combined? And is that incremental revenue where there are basically new programs or new capacity versus shifting from another region?

Rob Mionis - President & CEO
Look, what I can tell you, Matt is, how much square foot we're adding and that the capacity improvements are a couple of folds. One, phase 1, if you will, which is coming online this quarter is about 28,000 square feet of manufacturing space. It's really a AI/ML testing facility. So it's a test farm -- for fully automated test farm for all AI/ML products. So that's coming online right about now.
And then phase 2 will be the first half of 2025 and that's a combined productivity play of where we're combining all our warehousing in Thailand into one facility to save on space and drive productivity and also adding about 156,000 I mean 130,000 of plus of manufacturing space, which is going to support existing and new customers as well largely around AI/ML. And we think those capacity expansions should take care of us through the next couple of years of growth.

Matt Sheerin - Stifel
Okay. And just lastly, Mandeep, you talked about you basically increased your cash flow guidance for the year while keeping everything else intact. What are the reasons for that? Is that a function of the inventory reduction and working capital reduction and the cash flows from that or anything else?

Mandeep Chawla - CFO
Yeah. So we continue to be encouraged that the material environment is stabilizing and improving. We're seeing lead times right now, not necessarily at pre-pandemic levels for both passes (ph) and semis, but we are seeing them drop pretty close to that level and they've been improving quarter-to-quarter. We have been unwinding inventory as a result, so we're pleased that we're able to reduce some of that cash. Really strong finish 2023, $194 million, we believe that that is the right goal as a minimum for next year on the back of increasing profitability and an inventory environment that we think is going to continue to improve. And so we think the goal of $200 billion or more reflects a good level of conversion and is the right target at this time.

Matt Sheerin - Stifel
Okay. Thank you.

Mandeep Chawla - CFO
Thanks, Matt.

Operator
Thank you. We have our next question coming from the line of Todd Copeland from CIBC. Please go ahead.

Todd Coupland - CIBC
Hi. Great. Thanks, and good morning, everyone. I want to step back from these detailed questions and just ask a question on the hyperscaler market, data -- the global data center market. What's your view on how much of the data center hyperscaler market has been upgraded to support generative AI and large language model processing needs? How far into that cycle would you think we are at this point?

Rob Mionis - President & CEO
Good morning, Todd. That's a very good question. I would say, we're still in the early innings of the upgrade cycle. I mean, and I say that by the fact that it just started about a year or so ago, and given the amount of compute, which makes up about 50% of any data center that needs to kind of get upgraded, I think we're still in the very early innings of that upgrade cycle.

Todd Coupland - CIBC
Yeah. And the customers in terms of their cycles to get that upgraded a little bit longer than the quarter-to-quarter discussions is, I mean it's obviously going to be demand dependent, but is that a two-year process or five-year process what's the mindset towards getting that upgrade complete?

Rob Mionis - President & CEO
My sense is, it's a multi-year process. It's certainly five plus years. And again, across each of the hyperscalers that we're dealing with, each has different appetites and different phases for deployment so that they won't necessarily all overlap at once, which for at least for Celestica should give us many years of growth.

Mandeep Chawla - CFO
Yeah. I would add to that Todd. Again we support the top five hyperscalers, but not all the top five hyperscalers spend CapEx the same way and there's a couple in particular that sometimes are leading with the more complex technologies, and then the other hyperscalers sometimes follow. What we're really encouraged about is, where we're seeing a lot of our new winds come in and our demand outlook is with some of the hyperscalers that are at the leading edge of the more complex technologies. Hence, we're seeing the demand strengthen AI/ML computes, and we're seeing the wins come in on the 800G switches, some of which are starting to be shipped in ‘24, and then a lot more which will be shipped in 2025.
And as we see some of the other hyperscalers that follow behind that, it gives demands, it gives us an idea of the fact that this does have an opportunity to be a multi-year opportunity for us. And so when we -- and to Rob's point, we're really in the early stages right now of the AI/ML CapEx investment cycle. Of course nobody has visibility 10 years out on what things are going to look like, but we are seeing demand signals at least for the next two or three years.

Rob Mionis - President & CEO
And I would just close with, the adoption of some custom silicon is going to drive compute programs, and that's going to accelerate in the future. And then investments in AI is also going to drive advanced networking and that's going to be a driver in the future. And then also with our enterprise customers, we expect to see the Internet traffic is going to drive improvements in data center interconnect as well. So this whole upgrade cycle I think has a long life to it.

Todd Coupland - CIBC
Appreciate the color. Thanks a lot.

Rob Mionis - President & CEO
Thanks.

Operator
Thank you. There are no further questions at this time. I'd now like to turn the call back over to Mr. Rob Mionis for final closing comments.

Rob Mionis - President & CEO
Thank you. I'm pleased that we posted another solid quarter and the momentum is carrying through into the first quarter of 2024 and all through 2024. I'm also pleased by a continued strong execution and courage with a strong market position and growing markets. Thank you again for joining today's call and I look forward to updating you next quarter.

Operator
Thank you, sir. Ladies and gentlemen, this concludes your conference call for today. We thank you for participating and ask that you please disconnect your lines. Have a lovely day.
++++++++


"""