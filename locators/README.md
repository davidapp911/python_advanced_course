# Task Instructions
## PRACTICAL TASK: LOCATORS
For this practical task, any web browser that supports Developers' tools can be used.\
The main goal of the task:
- identify web elements required for executing test cases described below
- define reliable locators for these elements. 
### The following locator types MUST be used at least once:
- ID locator
- Name locator
- ClassName locator
- TagName locator
- LinkText locator
- PartialLinkText locator
- CSS locator (if possible, use pseudo-classes)
- XPath locator (Relative path)
- XPath locator with any operator
- XPath locator with axes \

### Elements and its locators should be presented in table form, like:
| Element         | Locator |
|-----------------|---------|
| "Search " Input | #search |
| ...             | ...     |

## Test Cases
### Test case #1. Validate that the user can search for a position based on criteria.
1. Navigate to https://www.epam.com/
2. Find a link “Carriers” and click on it
3. Write the name of any programming language in the field “Keywords” (should be taken from test
parameter)
4. Select “All Locations” in the “Location” field (should be taken from the test parameter)
5. Select the option “Remote”
6. Click on the button “Find”
7. Find the latest element in the list of results
8. Click on the button “View and apply”
9. Validate that the programming language mentioned in the step above is on a page

### Test case #2. Validate global search works as expected.
1. Navigate to https://www.epam.com/
2. Find a magnifier icon and click on it
3. Find a search string and put there “BLOCKCHAIN”/”Cloud”/”Automation” (use as a parameter for a test)
4. Click “Find” button
5. Validate that all links in a list contain the word “BLOCKCHAIN”/”Cloud”/”Automation” in the text.