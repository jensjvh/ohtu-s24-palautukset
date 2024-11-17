*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kimmo
    Set Password  kimmo123
    Confirm Password  kimmo123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ki
    Set Password  kimmo123
    Confirm Password  kimmo123
    Submit Credentials
    Register Should Fail With Message  Username is invalid

Register With Valid Username And Too Short Password
    Set Username  kimmo
    Set Password  kimmo12
    Confirm Password  kimmo12
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
    Set Username  kimmo
    Set Password  kimmokimmo
    Confirm Password  kimmokimmo
    Submit Credentials
    Register Should Fail With Message  Password should not consist of letters only

Register With Nonmatching Password And Password Confirmation
    Set Username  kimmo
    Set Password  kimmo123
    Confirm Password  kimmo124
    Submit Credentials
    Register Should Fail With Message  Password and confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Confirm Password  kalle123
    Submit Credentials
    Register Should Fail With Message  User already exists

Login After Successful Registration
    Go To Register Page
    Set Username  kimmo
    Set Password  kimmo123
    Confirm Password  kimmo123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  kimmo
    Set Password  kimmo123
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Go To Register Page
    Set Username  kimmo
    Set Password  kimmo123
    Confirm Password  kimmo124
    Submit Credentials
    Register Should Fail With Message  Password and confirmation do not match
    Go To Login Page
    Set Username  kimmo
    Set Password  kimmo123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Go To Register Page
    Go To  ${REGISTER_URL}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${confirm_pass}
    Input Password  password_confirmation  ${confirm_pass}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page