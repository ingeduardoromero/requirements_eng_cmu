import argparse
from goalmodeling.schema import *
    
nlp_search_query = Operation(
    name="Natural Language Search Query",
    category=OperationCategory.ENVIRONMENT_OPERATION
)
keyword_search_query = Operation(
    name="Keyword Search Query",
    category=OperationCategory.ENVIRONMENT_OPERATION
)
suggest_search_options = Operation(
    name="Suggest Search Options",
    category=OperationCategory.ENVIRONMENT_OPERATION
)
filter_within_search = Operation(
    name="Filter Within Search Results",
    category=OperationCategory.ENVIRONMENT_OPERATION
)

agent_user_nlp = Agent("User", AgentType.ENVIRONMENT_AGENT)
agent_user_keyword = Agent("User", AgentType.ENVIRONMENT_AGENT)
agent_user_suggest = Agent("User", AgentType.ENVIRONMENT_AGENT)
agent_user_filter = Agent("User", AgentType.ENVIRONMENT_AGENT)


agent_user_recent_searches = Agent("User", AgentType.ENVIRONMENT_AGENT)
agent_user_popular_terms = Agent("User", AgentType.ENVIRONMENT_AGENT)
achieve_keyword_search_if_simple_query = AchieveGoal(
    name="KeywordSearchIfSimpleQuery",
    performs=[PerformanceLink(agent_user_keyword, keyword_search_query)],
    refinements=None
)

achieve_filter_within_search_results = AchieveGoal(
    name="FilterWithinSearchResults",
    performs=[PerformanceLink(agent_user_filter, filter_within_search)],
    refinements=None
)

display_recent_searches = Operation(
    name="Open Search Bar",
    category=OperationCategory.ENVIRONMENT_OPERATION
)
suggest_popular_search_terms = Operation(
    name="Enter Most typed Search Terms",
    category=OperationCategory.ENVIRONMENT_OPERATION
)

achieve_display_recent_searches_if_available = AchieveGoal(
    name="DisplayRecentSearches <b>If</b> Available",
    performs=[PerformanceLink(agent_user_recent_searches, display_recent_searches)],
    refinements=None
)

achieve_suggest_popular_terms_based_on_activity = AchieveGoal(
    name="SuggestPopularTerms <b>If</b> SufficientActivity",
    performs=[PerformanceLink(agent_user_popular_terms, suggest_popular_search_terms)],
    refinements=None
)

achieve_suggest_search_options = AchieveGoal(
    name="SuggestSearchOptions",
    performs=None,
    refinements=[Refinement(
        complete=False,
        children=[
            achieve_display_recent_searches_if_available,
            achieve_suggest_popular_terms_based_on_activity
        ]
    )]
)


achieve_search_emails_using_nlp = AchieveGoal(
    name="SearchEmailsUsingNaturalLanguage",
    performs=None,
    refinements=[Refinement(
        complete=False,
        children=[
            achieve_keyword_search_if_simple_query,
            achieve_suggest_search_options,
            achieve_filter_within_search_results
        ]
    )]
)