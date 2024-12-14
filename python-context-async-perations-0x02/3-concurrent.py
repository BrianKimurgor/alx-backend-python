import aiosqlite

import asyncio

async def async_fetch_users():
    """
    Asynchronously fetches all user records from the 'users' table in the 'dental_clinic.db' SQLite database.

    This function establishes an asynchronous connection to the database, executes a SQL query to select all
    records from the 'users' table, retrieves all the results, and then closes the cursor before returning the data.

    Returns:
        list: A list of tuples, where each tuple represents a row from the 'users' table.
    """
    async with aiosqlite.connect("dental_clinic.db") as db:

        cursor = await db.execute("SELECT * FOM users")

        data = await cursor.fetchall()

        await cursor.close()

        return data


async def async_fetch_older_users():
    """
    Asynchronously fetches users older than 20 years from the 'users' table in the 'dental_clinic.db' database.

    Returns:
        list: A list of tuples, where each tuple represents a user record with all columns from the 'users' table.
    """
    async with aiosqlite.connect("dental_clinic.db") as db:
        # Execute the SQL query to select users older than 20
        cursor = await db.execute("SELECT * FROM users WHERE age > 20")

        # Fetch all results from the executed query
        data = await cursor.fetchall()

        # Close the cursor
        await cursor.close()
        
        return data


async def fetch_concurrently():
    """
    Asynchronously fetches user data concurrently using asyncio.gather.

    This function concurrently fetches two sets of user data:
    1. All users
    2. Users older than 40

    It then prints the results of both fetch operations.

    Returns:
        None
    """
    all_usrs, older_usrs = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    print("All users:")
    for row in all_usrs:
        print(row)
    

    print("\n All users that are Older than 40:")
    for row in older_usrs:
        print(row)

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())