def combine_md_files(input_files, output_file):
    with open(output_file, 'w', encoding='utf-8') as out:
        for file_path in input_files:
            with open(file_path, 'r', encoding='utf-8') as f:
                out.write(f.read() + '\n\n')

# Example usage:
input_files = ["prompt_engineering_pathway/Apricot Moose (Prompt Engineering Pathway) - DB 8cf2d59a35df4102bbe204f875ebdc10/Apricot Moose Prompt Generation General Workflow 1d51be7b4fd541fba9e66d3d7372088e.md", "prompt_engineering_pathway/Apricot Moose (Prompt Engineering Pathway) - DB 8cf2d59a35df4102bbe204f875ebdc10/How to Write Good Prompts to Enhance Safety cadf05d2434c451eb8a4eb613b4dc2ce.md", "prompt_engineering_pathway/Apricot Moose (Prompt Engineering Pathway) - DB 8cf2d59a35df4102bbe204f875ebdc10/Identifying Unsafe Content from Command 87f556f2a3bc4b22a0b0b29439cfc82b.md", "prompt_engineering_pathway/Apricot Moose (Prompt Engineering Pathway) - DB 8cf2d59a35df4102bbe204f875ebdc10/Invisible Safety General Guidelines a577393736404fd1a060d141c7953465.md", "prompt_engineering_pathway/My Hubs d6fb62a2ad9448beaeb8f812796cfc7e/Invisible Hub fac939897b4443018acd27d3fba8b78d/Directories 885af357d28d400eb0fc8fb3f450f4df/Apricot Moose - Training f4cf418c2a9f4350b22c05ff1dcc5360/Apricot Moose (Training) - DB 0a3b3e38d476449ea8a112be2ad1d24b/Cohere Safety Onboarding Pathway 62b5362cc332416e97fd57bbe6ddb311.md"]
output_file = "combined_file.md"
combine_md_files(input_files, output_file)
