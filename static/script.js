document.getElementById("transactionForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const description = document.getElementById("description").value;
    const amount = document.getElementById("amount").value;
    const userId = 1; // Replace with the actual user ID

    const responseMessage = document.getElementById("responseMessage");

    const csrftoken = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];

    const token = "14e5f12a44894d433bb6871c0685c1c79842eb71"; // Replace with the actual token

    try {
        const response = await fetch("http://127.0.0.1:8000/api/transactions/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,
                "Authorization": `Token ${token}`, // Include the token here
            },
            body: JSON.stringify({
                description: description,
                amount: amount,
            }),
        });

        if (response.ok) {
            const data = await response.json();
            responseMessage.textContent = "Transaction created successfully!";
            responseMessage.style.color = "green";
        } else {
            const errorData = await response.json();
            responseMessage.textContent = `Error: ${JSON.stringify(errorData)}`;
            responseMessage.style.color = "red";
        }
    } catch (error) {
        responseMessage.textContent = `Error: ${error.message}`;
        responseMessage.style.color = "red";
    }
});