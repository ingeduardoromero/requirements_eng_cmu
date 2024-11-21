flowchart BT
node81((" ")) ===> node82[/"Achieve[KeepUpToDateCompanyCommunicationUsingEmailClient]"/]
node80[/"Achieve[OpenedEmailClient]"/] --- node81
annotationnode12["AND Refinement"]:::stroke -.- node81
annotationnode1["Functional Requirement"]:::stroke -.- node80
node78((" ")):::filled ===> node80[/"Achieve[OpenedEmailClient]"/]
node71[/"Achieve[OpenedEmailWebClient]"/] --- node78
node70((" ")) ===> node71[/"Achieve[OpenedEmailWebClient]"/]
annotationnode6["OR Refinement"]:::stroke -.- node78
annotationnode10["Milestone Refinement"]:::stroke -.- node70
node64[/"Achieve[OpenedBrowser <b>If Not</b> Open]"/] --- node70
node63((" ")) ===> node64[/"Achieve[OpenedBrowser <b>If Not</b> Open]"/]
node62[/"Achieve[OpenedBrowser]"/] --- node63
node61((" ")) ===> node62[/"Achieve[OpenedBrowser]"/]
node57[/"Achieve[DoubleClickBrowserIcon]"/] --- node61
node56{{fa:fa-person User}} --- node57
node55(["Double click on Browser Icon"]) --- node56
node60[/"Achieve[KeyboardInputBrowserNameAndReturnKey]"/] --- node61
node59{{fa:fa-person User}} --- node60
node58(["Type Command+Space bar and type Browser Name"]) --- node59


node69[/"Achieve[OpenedNewBrowserTab <b>If</b> Browser already Open]"/] --- node70
node68((" ")) ===> node69[/"Achieve[OpenedNewBrowserTab <b>If</b> Browser already Open]"/]
node67[/"Achieve[OpenedNewTab]"/] --- node68
node66{{fa:fa-person User}} --- node67
node65(["Click New Tab Button"]) --- node66



node79((" ")):::filled ===> node80[/"Achieve[OpenedEmailClient]"/]
annotationnode11["OR Refinement"]:::stroke -.- node79
node74[/"Achieve[OpenedEmailMobileApp]"/] --- node79
node73{{fa:fa-person User}} --- node74
node72(["Open Applications Folder and Open Email App"]) --- node73
node77[/"Maintain[OpenedEmailMobileApp]"/] --- node79
node76{{fa:fa-person User}} --- node77
node75(["keep Opened Email Mobile App"]) --- node76

node53[/"Achieve[OrganizedEmailsIfNotAlready]"/] --- node81
node52((" ")) ===> node53[/"Achieve[OrganizedEmailsIfNotAlready]"/]
annotationnode7["Decomposition By case"]:::stroke -.- node52
annotationnode2["Non Functional Requirement"]:::stroke -.- node53
node35[/"Achieve[ArchivedSingleEmailIfOneSelected]"/]:::bold --- node52
node33{{fa:fa-person User}} --- node35
node31(["Archive Single Email"]) --- node33
node36[/"Achieve[ArchivedMultipleMailsIfMultipleSelection]"/]:::bold --- node52
node34{{fa:fa-person User}} --- node36
node32(["Archive Multiple Emails"]) --- node34
node48[/"Achieve[HandlePhishingEmailsIfIdentified]"/] --- node52
annotationnode5["Behavioural Requirement"]:::stroke -.- node48
annotationnode8["Uncontrollability Refinement"]:::stroke -.- node48
node46((" ")):::filled ===> node48[/"Achieve[HandlePhishingEmailsIfIdentified]"/]
node43[/"Achieve[MarkEmailAsPhishingIfEmailisDetectedasSuspicious]"/]:::bold --- node46
node40{{fa:fa-person User}} --- node43
node37(["Mark Email as Phishing"]) --- node40

node47((" ")):::filled ===> node48[/"Achieve[HandlePhishingEmailsIfIdentified]"/]
node44[/"Achieve[MoveEmailToSpamFolder]"/]:::bold --- node47
node41{{fa:fa-person User}} --- node44
node38(["Move Email to Spam Folder"]) --- node41

node51[/"Achieve[MarkEmailAsRead]"/]:::bold --- node52
node50{{fa:fa-person User}} --- node51
node49(["Mark Email as Read"]) --- node50

node30[/"Achieve[SearchEmailsUsingNaturalLanguage]"/] --- node81
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

node10[/"Achieve[HandleAsyncChatMessages]"/] --- node81
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



classDef bold stroke-width:3,stroke:#000
classDef filled fill:#000;
classDef nostroke stroke-width:0,fill-opacity:0.0
classDef stroke stroke-dasharray: 5 5,fill-opacity:0.0,text-align:left