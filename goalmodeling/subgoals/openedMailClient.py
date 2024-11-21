import argparse
from goalmodeling.schema import *

agent_user0 = Agent("User", AgentType.ENVIRONMENT_AGENT)


keep_run_window_in_foreground = Operation(
    name="Double click on Browser Icon",
    category=OperationCategory.ENVIRONMENT_OPERATION)

agent_user1 = Agent("User", AgentType.ENVIRONMENT_AGENT)

maintain_run_window_in_foreground = AchieveGoal(
    name="DoubleClickBrowserIcon",
    performs=[PerformanceLink(agent_user1, keep_run_window_in_foreground)])

type_browser_name_and_return_key = Operation(
    "Type Command+Space bar and type Browser Name",
    OperationCategory.ENVIRONMENT_OPERATION)

agent_user3 = Agent("User", AgentType.ENVIRONMENT_AGENT)

achieve_keyboard_input_chrome_exe_and_return_key = AchieveGoal(
    name="KeyboardInputBrowserNameAndReturnKey",
    performs=[PerformanceLink(agent_user3, type_browser_name_and_return_key)])

achieve_opened_browser = AchieveGoal("OpenedBrowser", None, [
    Refinement(
        complete=False,
        children=[
            maintain_run_window_in_foreground,
            achieve_keyboard_input_chrome_exe_and_return_key]
    )
])

achieve_opened_browser_if_not_already_open_browser = AchieveGoal(
    name="OpenedBrowser <b>If Not</b> Open",
    refinements=[
        Refinement(
            complete=False,
            children=[achieve_opened_browser]
        )
    ])

click_new_tab_button = Operation(
    name="Click New Tab Button",
    category=OperationCategory.ENVIRONMENT_OPERATION)

agent_user4 = Agent("User", AgentType.ENVIRONMENT_AGENT)

achieve_opened_new_browser_tab = AchieveGoal(
    name="OpenedNewTab",
    performs=[PerformanceLink(agent_user4, operation=click_new_tab_button)])

achieve_opened_new_browser_tab_if_browser_already_open = AchieveGoal(
    
name="OpenedNewBrowserTab <b>If</b> Browser already Open",
    refinements=[
        Refinement(
            complete=False,
            children=[achieve_opened_new_browser_tab]
        )
    ])

achieve_opened_web_client = AchieveGoal(
    name="OpenedEmailWebClient",
    refinements=[
        Refinement(
            complete=False,
            children=[
                achieve_opened_browser_if_not_already_open_browser,
                achieve_opened_new_browser_tab_if_browser_already_open]
        )
    ])

open_applications_folder_and_open_email_app = Operation(
    "Open Applications Folder and Open Email App",
    OperationCategory.ENVIRONMENT_OPERATION)

agent_user2 = Agent("User", AgentType.ENVIRONMENT_AGENT)

achieve_opened_mobile_client = AchieveGoal(
    name="OpenedEmailMobileApp",
    performs=[PerformanceLink(agent_user2, open_applications_folder_and_open_email_app)])

maintain_opened_mobile_app = Operation(
    "keep Opened Email Mobile App",
    OperationCategory.ENVIRONMENT_OPERATION)

agent_user5 = Agent("User", AgentType.ENVIRONMENT_AGENT)

maintain_opened_mobile_app = MaintainGoal(
    name="OpenedEmailMobileApp",
    performs=[PerformanceLink(agent_user5, maintain_opened_mobile_app)])

achieve_opened_email_client = AchieveGoal(
    name="OpenedEmailClient",
    refinements=[
        Refinement(
            complete=True,
            children=[
                achieve_opened_web_client
            ]
        ),
        Refinement(
            complete=True,
            children=[
                achieve_opened_mobile_client,
                maintain_opened_mobile_app
            ]
        )
    ])
                