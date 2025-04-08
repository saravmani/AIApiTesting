import os
from dotenv import load_dotenv
from modules.TestCasesSelfHealer import TestCasesSelfHealer
from modules.BDDSelfHealer import BDDSelfHealer
from modules.ModifiedBddFinder import ModifiedBddFinder
from modules.BDDValidator import BDDValidator
from modules.APITestCaseGenerator import APITestCaseGenerator
from modules.BDDGenerator import BddGenerator
from Tools.TestDataGeneratorTool import SwaggerTestDataGenerator
import json
load_dotenv()
 

def remove_code_blocks(text, lang): 
  text = text.replace("```"+lang, "")
  text = text.replace("```", "")
  text = text.replace("TERMINATE", "")
  return text.strip() 



input(
    "\n👋 Hi! I am your Gen AI Tool.\n"
    "I can help you with the following:\n"
    "• Generate automated BDD Features and PyTest test cases\n"
    "• Assist in Self-Healing of existing BDD and PyTest test cases\n\n"
    "➡️ Press Enter to get started..."
)

user_input_choice = input(
    "\nPlease select an option to proceed:\n"
    "1️⃣  Generate BDD and PyTest test cases for your API\n"
    "2️⃣  Generate PyTest test cases for existing BDD test cases\n"
    "3️⃣  Self-heal your existing BDD and PyTest test cases\n\n"
    "Enter your choice (1/2/3): "
)





api_base_url = input("\n🔗 Enter the base API URL (e.g., http://localhost:8080): ")
api_swagger_url = input("📄 Enter the OpenAPI/Swagger URL (e.g., http://localhost:8080/v3/api-docs): ")


# api_base_url=   "http://localhost:8080"
# api_swagger_url =  "http://localhost:8080"+"/v3/api-docs"


print("\n📡 Accessing OpenAPI documentation to analyze API endpoints and parameters...")


generator = SwaggerTestDataGenerator(api_swagger_url)
test_data_dictionary = generator.generate_test_data_for_all_endpoints()



if user_input_choice=="1":
      


  ########################################################################


  for api_url, test_data in test_data_dictionary.items():
    print(f"\n🛠️ Generating BDD test cases for API: {api_url}")
    try:
      apiname = api_url.replace("/","_") 
      test_data=json.dumps(test_data_dictionary[api_url])

      # BddGenerator:
      bdd_generator = BddGenerator(api_url,test_data)
      task_statement = "Generate BDD Test cases in gherkin language, for the API with the given context, API parameters, API information. Api URL :  "+api_url
      answer = bdd_generator.generate_bdd_test_cases(task_statement)
      cleaned_text = remove_code_blocks(answer,"gherkin")
    
    except Exception as e:
              print(f"Error generating BDD test cases: {e}")


  print("\n✅ BDD test cases generation completed.")
  print("🔧 Launching BDD validator for any updates...\n")
  ## GEN AI Helper for users to update the BDD test cases
  bdd_validator = BDDValidator()
  bdd_validator.update_bdd();
  
  print("\n✅ BDD test cases have been updated successfully.")

if user_input_choice=="1":
  user_input_choice = input("➡️ Enter '2' to proceed with generating PyTest test cases based on updated BDDs: ")


  #######################################################################
if user_input_choice=="2":
  print("\n🛠️ Generating PyTest test cases from BDD test data...")
  api_Test_Case_Generator = APITestCaseGenerator(api_base_url) 
  answer = api_Test_Case_Generator.generate_pytest_testcases(test_data_dictionary)
  print("\n✅ PyTest test case generation completed successfully.")
  print("***************************************")



if user_input_choice=="3":
  print("\n🔍 Scanning modified BDD files that need healing...")
  modified_bddFinder = ModifiedBddFinder("","")
  bdd_files_needs_to_be_updated = modified_bddFinder.update_bbd_test_cases()
  # print(bdd_files_needs_to_be_updated)

  ## bdd_files_needs_to_be_updated = {'api_urls_with_content_modified': [{'url': '/api/users/register', 'content': 'The Phone number length should be 15. if this rule not passed then api should return 400.'}, {'url': '/api/users/login', 'content': 'Authenticates users by accepting email address. And Email address domain should be "gmail.com / yahoo.com" and password and generates a JWT token.'}]}
  print("🧬 Healing BDD files...")
  BDD_self_healer = BDDSelfHealer()
  BDD_self_healer.heal_bdd_files(bdd_files_needs_to_be_updated)


  BDD_self_healer = TestCasesSelfHealer()
  BDD_self_healer.heal_test_files(bdd_files_needs_to_be_updated)

  print("\n✅ Self-healing process completed.")
  print("***************************************")

