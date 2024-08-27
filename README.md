# PLP_Academy
#Evening Session

<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Title -->
    <title>Expense Tracker Application</title>

    <!-- Meta tags -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Track your expenses efficiently with our application.">

    <!-- External CSS or Inline Styles -->
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }

        header {
            background-color: #4CAF50;
            padding: 10px;
            text-align: center;
            color: white;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }

        table, th, td {
            border: 1px solid #ddd;
        }

        th, td {
            padding: 10px;
            text-align: left;
        }

        th {
            background-color: #4CAF50;
            color: white;
        }

        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto;
        }

        form {
            margin: 20px 0;
        }

        label {
            display: block;
            margin: 10px 0 5px;
        }

        input[type="text"], input[type="email"], input[type="tel"] {
            width: 100%;
            padding: 8px;
            margin: 5px 0 10px;
            box-sizing: border-box;
        }

        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            cursor: pointer;
        }
    </style>
</head>

<body>

    <!-- Header -->
    <header>
        <h1>Expense Tracker Application</h1>
    </header>

    <!-- Heading -->
    <h2>Welcome to Your Expense Tracker</h2>

    <!-- Paragraph -->
    <p>Manage your daily expenses easily and efficiently with our expense tracker application.</p>

    <!-- Basic Registration Form -->
    <form>
        <h3>Register</h3>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required>

        <input type="submit" value="Register">
    </form>

    <!-- Table Displaying Common User Information -->
    <table>
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone Number</th>
        </tr>
        <tr>
            <td>John Doe</td>
            <td>john.doe@example.com</td>
            <td>123-456-7890</td>
        </tr>
        <tr>
            <td>Jane Smith</td>
            <td>jane.smith@example.com</td>
            <td>098-765-4321</td>
        </tr>
    </table>

    <!-- Image -->
    <img src="https://via.placeholder.com/400x200" alt="Expense Tracker">

    <!-- External Link -->
    <p>For more information, visit <a href="https://google.com" target="_blank">Google</a>.</p>

</body>

</html>
