import argparse
from blog_generator import generate_blog, save_to_file

parser = argparse.ArgumentParser()
parser.add_argument("topic", help="Topic to write about")
parser.add_argument("--tone", default="neutral", help="Tone of writing")
parser.add_argument("--language", default="English", help="Language")
parser.add_argument("--save", action="store_true", help="Save to file")
args = parser.parse_args()

blog = generate_blog(args.topic, args.tone, args.language)
print("\nGenerated Blog Paragraph:\n")
print(blog)

if args.save:
    save_to_file(blog)
