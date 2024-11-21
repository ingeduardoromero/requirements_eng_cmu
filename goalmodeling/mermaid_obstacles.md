flowchart BT
node86((" ")) ===> node87[/"Achieve[KeepUpToDateCompanyCommunicationUsingEmailClient]"/]
node85[/"Achieve[OpenedEmailClient]"/] --- node86
annotationnode12["AND Refinement"]:::stroke -.- node86
annotationnode1["Functional Requirement"]:::stroke -.- node85
node83((" ")):::filled ===> node85[/"Achieve[OpenedEmailClient]"/]
node76[/"Achieve[OpenedEmailWebClient]"/] --- node83
node75((" ")) ===> node76[/"Achieve[OpenedEmailWebClient]"/]
annotationnode6["OR Refinement"]:::stroke -.- node83
annotationnode10["Milestone Refinement"]:::stroke -.- node75
node69[/"Achieve[OpenedBrowser <b>If Not</b> Open]"/] --- node75
node68((" ")) ===> node69[/"Achieve[OpenedBrowser <b>If Not</b> Open]"/]
node67[/"Achieve[OpenedBrowser]"/] --- node68
node66((" ")) ===> node67[/"Achieve[OpenedBrowser]"/]
node62[/"Achieve[DoubleClickBrowserIcon]"/] --- node66
node61{{fa:fa-person User}} --- node62
node60(["Double click on Browser Icon"]) --- node61
node65[/"Achieve[KeyboardInputBrowserNameAndReturnKey]"/] --- node66
node64{{fa:fa-person User}} --- node65
node63(["Type Command+Space bar and type Browser Name"]) --- node64




node74[/"Achieve[OpenedNewBrowserTab <b>If</b> Browser already Open]"/] --- node75
node73((" ")) ===> node74[/"Achieve[OpenedNewBrowserTab <b>If</b> Browser already Open]"/]
node72[/"Achieve[OpenedNewTab]"/] --- node73
node71{{fa:fa-person User}} --- node72
node70(["Click New Tab Button"]) --- node71






node84((" ")):::filled ===> node85[/"Achieve[OpenedEmailClient]"/]
annotationnode11["OR Refinement"]:::stroke -.- node84
node79[/"Achieve[OpenedEmailMobileApp]"/] --- node84
node78{{fa:fa-person User}} --- node79
node77(["Open Applications Folder and Open Email App"]) --- node78
node82[/"Maintain[OpenedEmailMobileApp]"/] --- node84
node81{{fa:fa-person User}} --- node82
node80(["keep Opened Email Mobile App"]) --- node81


node58[/"Achieve[OrganizedEmailsIfNotAlready]"/] --- node86
node57((" ")) ===> node58[/"Achieve[OrganizedEmailsIfNotAlready]"/]
annotationnode7["Decomposition By case"]:::stroke -.- node57
annotationnode2["Non Functional Requirement"]:::stroke -.- node58
node35[/"Achieve[ArchivedSingleEmailIfOneSelected]"/]:::bold --- node57
node33{{fa:fa-person User}} --- node35
node31(["Archive Single Email"]) --- node33
node36[/"Achieve[ArchivedMultipleMailsIfMultipleSelection]"/]:::bold --- node57
node34{{fa:fa-person User}} --- node36
node32(["Archive Multiple Emails"]) --- node34
node53[/"Achieve[HandlePhishingEmailsIfIdentified]"/] --- node57
annotationnode5["Behavioural Requirement"]:::stroke -.- node53
annotationnode8["Uncontrollability Refinement"]:::stroke -.- node53
node51((" ")):::filled ===> node53[/"Achieve[HandlePhishingEmailsIfIdentified]"/]
node48[/"Achieve[MarkEmailAsPhishing]"/]:::bold --- node51
node40{{fa:fa-person User}} --- node48
node37(["Mark Email as Phishing"]) --- node40


node47[\"<b>Not Identify Phishing Emails</b>"\]
node47 ---x node48


node45((" ")) ===> node47
node43[\"Phishing Email Not categorized"\] --- node45


node46((" ")) ===> node47
node44[\"Advanced Phishing Email arrived"\] --- node46


node50[/"Adjusted more Visual Labeling"/]:::bold ---x node43
node88[/"Better Security Agent model"/]:::bold ---x node44


node52((" ")):::filled ===> node53[/"Achieve[HandlePhishingEmailsIfIdentified]"/]
node49[/"Achieve[MoveEmailToSpamFolder]"/]:::bold --- node52
node41{{fa:fa-person User}} --- node49
node38(["Move Email to Spam Folder"]) --- node41


node56[/"Achieve[MarkEmailAsRead]"/]:::bold --- node57
node55{{fa:fa-person User}} --- node56
node54(["Mark Email as Read"]) --- node55


node30[/"Achieve[SearchEmailsUsingNaturalLanguage]"/] --- node86
annotationnode3["Functional Requirement"]:::stroke -.- node30
annotationnode9["Decomposition by case"]:::stroke -.- node29
node29((" ")) ===> node30[/"Achieve[SearchEmailsUsingNaturalLanguage]"/]
node21[/"Achieve[KeywordSearchIfSimpleQuery]"/] --- node29
node16{{fa:fa-person User}} --- node21
node12(["Keyword Search Query"]) --- node16
node28[/"Achieve[SuggestSearchOptions]"/] --- node29
node27((" ")) ===> node28[/"Achieve[SuggestSearchOptions]"/]
node25[/"Achieve[DisplayRecentSearches <b>If</b> Available]"/] --- node27
node19{{fa:fa-person User}} --- node25
node23(["Open Search Bar"]) --- node19
node26[/"Achieve[SuggestPopularTerms <b>If</b> SufficientActivity]"/] --- node27
node20{{fa:fa-person User}} --- node26
node24(["Enter Most typed Search Terms"]) --- node20


node22[/"Achieve[FilterWithinSearchResults]"/] --- node29
node18{{fa:fa-person User}} --- node22
node14(["Filter Within Search Results"]) --- node18


node10[/"Achieve[HandleAsyncChatMessages]"/] --- node86
annotationnode13["AND Refinement"]:::stroke -.- node9
node9((" ")) ===> node10[/"Achieve[HandleAsyncChatMessages]"/]
node6[/"Achieve[CreateMessageThread <b>If</b> ConversationNeedsOrganization]"/] --- node9
node3{{fa:fa-person User}} --- node6
node0(["Create Message Thread"]) --- node3
node7[/"Achieve[RespondToSpecificThread]"/] --- node9
node4{{fa:fa-person User}} --- node7
node1(["Respond to Thread"]) --- node4
node8[/"Achieve[ReactToMessage <b>If</b> AcknowledgmentNeeded]"/] --- node9
annotationnode4["Soft Requirement"]:::stroke -.- node8
node5{{fa:fa-person User}} --- node8
node2(["React to Message"]) --- node5


node89[\"<b>Not Able to Handle Chat load</b>"\]
node89 ---x node10


node90((" ")) ===> node89
node91[\"Limited Configured Reliability"\] --- node90


node92[/"Increased number of Servers"/]:::bold ---x node91

classDef bold stroke-width:3,stroke:#000
classDef filled fill:#000;
classDef nostroke stroke-width:0,fill-opacity:0.0
classDef stroke stroke-dasharray: 5 5,fill-opacity:0.0,text-align:left