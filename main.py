import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

# Database Connection
# NOTE: Replace 'your_password' with the actual MySQL root password
try:
    con = sqlt.connect(host="localhost", user="root", passwd="your_password", database="social_media")
    cursor = con.cursor()
except sqlt.Error as err:
    print(f"Database Connection Error: {err}")
    exit() # Exit if connection fails

# ==============================================================================
# 1. USER MANAGEMENT FUNCTIONS
# ==============================================================================

def user_input():
    # Function to add new user details to the 'user' table
    try:
        userid = int(input("Enter New User ID: "))
        username = input("Enter Username: ")
        email = input("Enter Email: ")
        city = input("Enter City: ")
        phone = input("Enter Phone No: ")
        join_date = input("Enter Join Date (YYYY-MM-DD): ")
    
        qry = "INSERT INTO user VALUES ({},'{}','{}','{}','{}','{}');".format(userid, username, email, city, phone, join_date)
        cursor.execute(qry)
        con.commit()
        print("\nSUCCESS: User registered successfully..")
    except Exception as e:
        print(f"\nERROR: Wrong Entry or Duplicate ID/Username/Email! Details: {e}")

def user_edit():
    # Function to update a user's details (e.g., city)
    x = int(input("Enter User ID to edit: "))
    qry = "SELECT * FROM user WHERE userid = {};".format(x)
    cursor.execute(qry)
    if cursor.fetchone():
        y = input("Enter New City: ")
        qry = "UPDATE user SET city = '{}' WHERE userid = {};".format(y, x)
        cursor.execute(qry)
        con.commit()
        print("\nSUCCESS: User details edited successfully.")
    else:
        print("\nALERT: Wrong User ID. User not found.")

def user_delete():
    # Function to delete a user and cascade delete related posts/comments
    x = int(input("Enter User ID to delete: "))
    qry = "SELECT * FROM user WHERE userid = {};".format(x)
    cursor.execute(qry)
    if cursor.fetchone():
        # Deletion will cascade due to FK definition in MySQL
        qry = "DELETE FROM user WHERE userid = {};".format(x)
        cursor.execute(qry)
        con.commit()
        print("\nSUCCESS: User and all associated data deleted successfully.")
    else:
        print("\nALERT: Wrong User ID. Deletion failed.")

def user_search():
    # Function to search and display details of a specific user
    x = int(input("Enter User ID to search: "))
    qry = "SELECT * FROM user WHERE userid = {};".format(x)
    df = pd.read_sql(qry, con)
    if not df.empty:
        print("\nSearch Result:")
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
    else:
        print("\nALERT: Wrong User ID. User not found.")

def user_output():
    # Function to display all records from the 'user' table
    df = pd.read_sql("SELECT * FROM user", con)
    if not df.empty:
        print("\n--- ALL USER RECORDS ---")
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
    else:
        print("\nALERT: No user records found.")


# ==============================================================================
# 2. POST MANAGEMENT FUNCTIONS
# ==============================================================================

def post_input():
    # Function to allow a user to create a new post
    try:
        userid = int(input("Enter User ID creating the post: "))
        # Check if user exists
        cursor.execute("SELECT * FROM user WHERE userid = {};".format(userid))
        if not cursor.fetchone():
            print("\nERROR: User ID does not exist. Post creation aborted.")
            return

        # Simple Auto-generate postid
        cursor.execute("SELECT MAX(postid) FROM posts;")
        r = cursor.fetchone()[0]
        postid = (r + 1) if r else 1

        content = input("Enter Post Content (max 255 chars): ")
        post_date = input("Enter Post Date (YYYY-MM-DD): ")
        
        qry = "INSERT INTO posts (postid, userid, post_content, post_date, likes) VALUES ({},{},'{}','{}',0);".format(
            postid, userid, content, post_date)
        cursor.execute(qry)
        con.commit()
        print("\nSUCCESS: Post created successfully.. Post ID:", postid)
    except Exception as e:
        print(f"\nERROR: Invalid entry or database issue. Details: {e}")

def post_delete():
    # Function to delete a post by its ID
    x = int(input("Enter Post ID to delete: "))
    qry = "SELECT * FROM posts WHERE postid = {};".format(x)
    cursor.execute(qry)
    if cursor.fetchone():
        # Deletion will cascade due to FK definition (deleting related comments)
        qry = "DELETE FROM posts WHERE postid = {};".format(x)
        cursor.execute(qry)
        con.commit()
        print("\nSUCCESS: Post and associated comments deleted successfully.")
    else:
        print("\nALERT: Wrong Post ID. Deletion failed.")

def post_output():
    # Function to display all posts, joining with user table for username
    qry = """
    SELECT P.postid, U.username, P.post_content, P.likes, P.post_date 
    FROM posts P JOIN user U ON P.userid = U.userid ORDER BY P.post_date DESC
    """
    df = pd.read_sql(qry, con)
    if not df.empty:
        print("\n--- ALL POSTS ---")
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
    else:
        print("\nALERT: No posts found.")

# ==============================================================================
# 3. REPORTING FUNCTIONS (DATA VISUALIZATION)
# ==============================================================================

def active_user_chart():
    """Generates a chart of the top 5 most active users based on post count."""
    q = """
    SELECT U.username, COUNT(P.postid) AS total_posts 
    FROM posts P JOIN user U ON P.userid = U.userid 
    GROUP BY U.username ORDER BY total_posts DESC LIMIT 5;
    """
    df = pd.read_sql(q, con)
    
    if df.empty:
        print("\nALERT: No posts data available to generate the Active Users report.")
        return

    print("\nData for Top 5 Most Active Users (by Posts):")
    print(df)
    
    plt.figure(figsize=(10, 6))
    plt.bar(df.username, df.total_posts, color=['#4CAF50', '#2196F3', '#FFC107', '#FF5722', '#9C27B0'])
    plt.xlabel("Username")
    plt.ylabel("Total Posts")
    plt.title("Top 5 Most Active Users on the Platform")
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()

def most_liked_chart():
    """Generates a chart of the top 5 most liked posts."""
    q = "SELECT postid, likes FROM posts ORDER BY likes DESC LIMIT 5;"
    df = pd.read_sql(q, con)
    
    if df.empty:
        print("\nALERT: No posts data available to generate the Most Liked report.")
        return

    print("\nData for Top 5 Most Liked Posts:")
    print(df)

    plt.figure(figsize=(10, 6))
    plt.bar(df.postid.astype(str), df.likes, color='lightcoral')
    plt.xlabel("Post ID")
    plt.ylabel("Number of Likes")
    plt.title("Top 5 Most Liked Posts (Engagement Metric)")
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()

# ==============================================================================
# 4. MAIN MENU AND CONTROL LOGIC
# ==============================================================================

while(True):
    print("="*78)
    print("\t\t\t------Social Media User Management System------\n")
    print("="*78)
    print("\t\t\t\tMAIN MENU\n\t\t\t\t1. User Details\n\t\t\t\t2. Post Management\n\t\t\t\t3. Reports\n\t\t\t\t4. Exit")
    try:
        choice = int(input("Enter Choice (1-4): "))
    except ValueError:
        print("\nINVALID INPUT. Please enter a number from the menu.\n")
        continue

    if choice == 1:
        while(True):
            print("\n\t\t\t\t--- User Details Sub-Menu ---\n\t\t\t\t1. Add New User\n\t\t\t\t2. Edit User City\
            \n\t\t\t\t3. Delete A User\n\t\t\t\t4. Search A User\n\t\t\t\t5. View All Users\n\t\t\t\t6. Back To Main Menu")
            try:
                ch = int(input("Enter Choice (1-6): "))
            except ValueError:
                print("\nINVALID INPUT. Please enter a number.\n")
                continue

            if ch == 1:
                user_input()
            elif ch == 2:
                user_edit()
            elif ch == 3:
                user_delete()
            elif ch == 4:
                user_search()
            elif ch == 5:
                user_output()
            elif ch == 6:
                break
            else:
                print("\nINVALID CHOICE. Please select from 1 to 6.")

    elif choice == 2:
        while(True):
            print("\n\t\t\t\t--- Post Management Sub-Menu ---\n\t\t\t\t1. Create New Post\n\t\t\t\t2. Delete A Post\
            \n\t\t\t\t3. View All Posts\n\t\t\t\t4. Back To Main Menu")
            try:
                ch = int(input("Enter Choice (1-4): "))
            except ValueError:
                print("\nINVALID INPUT. Please enter a number.\n")
                continue

            if ch == 1:
                post_input()
            elif ch == 2:
                post_delete()
            elif ch == 3:
                post_output()
            elif ch == 4:
                break
            else:
                print("\nINVALID CHOICE. Please select from 1 to 4.")

    elif choice == 3:
        while(True):
            print("\n\t\t\t\t--- Reports Sub-Menu ---\n\t\t\t\t1. Most Active Users (Chart)\
            \n\t\t\t\t2. Most Liked Posts (Chart)\n\t\t\t\t3. Back to Main Menu")
            try:
                ch = int(input("Enter Choice (1-3): "))
            except ValueError:
                print("\nINVALID INPUT. Please enter a number.\n")
                continue

            if ch == 1:
                active_user_chart()
            elif ch == 2:
                most_liked_chart()
            elif ch == 3:
                break
            else:
                print("\nINVALID CHOICE. Please select from 1 to 3.")

    elif choice == 4:
        print("\nExiting Social Media User Management System. Thank you for using the application!")
        con.close()
        break
    
    else:
        print("\nINVALID CHOICE. Please select from 1 to 4.")
