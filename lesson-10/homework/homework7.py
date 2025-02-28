

class Post:
    def __init__(self,title,content,author):
        self.title = title
        self.content = content
        self.author = author
    def __str__(self):
        return f'Title: {self.title} Content: {self.content} Author: {self.author}'


class Blog:
    def __init__(self):
        self.posts = []
    def add_post(self,title,content,author):
        post = Post(title,content,author)
        self.posts.append(post)
        print('Post has been successfully uploaded.')
    def list_all_posts(self):
        if not self.posts:
            print('No post available! ')
        else:
            print('Here is all blog posts. ')
            for ind, post in enumerate(self.posts, start=1):
                print(f'Post {ind}: {post} ')
    def post_by_specific_author(self,author):
        specific_post = [post for post in self.posts if post.author == author ]
        if not specific_post:
            print(f'No post avaialbe under {author}')
        else:
            print(f'This is post by {author}')
            for post in specific_post:
                print(post)
    def delete_post(self,number_post):
        try:
            del self.posts[number_post]
            print("Post deleted successfully! ")
        except IndexError:
            print("Invalid post number! ")
    def edit_post(self, number_post,new_title,new_content):
        if not self.posts:
            print('No post available to edit. ')
            return
        if 0 <= number_post <= len(self.posts):
            old_title = self.posts[number_post].title
            self.posts[number_post].title = new_title.strip()
            self.posts[number_post].content = new_content.strip()

            print('The post has been successfully edited. ')
        else:
            print('No post available under this number. Please try another post number.')
    def display_latest_post(self):
        if self.posts:
            print('Here is latest post. ')
            print(self.posts[-1])
        else:
            print('No latest post available. ')



def main():
    blog = Blog()

    while True:
        print("\nSimple Blog System")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Display Latest Post")
        print("7. Exit")

        choice = input('Enter your choice: ')

        if choice == '1':
            title = input('Enter your title: ')
            content = input('Enter your post content: ')
            authon = input('Enter authon name: ')
            blog.add_post(title,content,authon)
        elif choice == '2':
            blog.list_all_posts()
        elif choice == '3':
            authon = input('Enter authon name: ')
            blog.post_by_specific_author(authon)
        elif choice == '4':
            blog.list_all_posts()
            try:
                number_post = int(input("Enter post number to delete: ")) - 1
                blog.delete_post(number_post)
            except ValueError:
                print("Please enter a valid number. ")
        elif choice == '5':
            blog.list_all_posts()
            number_post = int(input('Post number to edit: ')) -1
            new_title = input('Enter new title: ')
            new_content = input('Enter new content: ')
            blog.edit_post(number_post,new_content,new_content)
        elif choice == '6':
            blog.display_latest_post()
        elif choice == '7':
            print('Thank you entering our blog system! ')
            break

if __name__ == "__main__":
    main()




    