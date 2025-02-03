document.addEventListener('DOMContentLoaded', () => {
    const toggleAdmin = document.getElementById('toggleAdmin');
    const adminSection = document.getElementById('adminSection');
    const adminFunctions = document.getElementById('adminFunctions');
    const addMemberBtn = document.getElementById('addMemberBtn');
    const addMemberForm = document.getElementById('addMemberForm');
    const loginBtn = document.getElementById('loginBtn');

    // Toggle Admin Section Visibility
    toggleAdmin.addEventListener('click', () => {
        adminSection.classList.toggle('hidden');
    });

    // Handle Admin Login
    loginBtn.addEventListener('click', async () => {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        const response = await fetch('/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password }),
        });

        const result = await response.json();
        if (response.ok) {
            alert(result.message);
            adminSection.classList.add('hidden');
            adminFunctions.classList.remove('hidden');
        } else {
            alert(result.error);
        }
    });

    // Toggle Add Member Form
    addMemberBtn.addEventListener('click', () => {
        addMemberForm.classList.toggle('hidden');
    });

    // Handle Add Member
    document.getElementById('submitMember').addEventListener('click', async () => {
        const name = document.getElementById('memberName').value;
        const phone = document.getElementById('memberPhone').value;

        const response = await fetch('/add-member', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, phone_number: phone }),
        });

        const result = await response.json();
        if (response.ok) {
            alert(result.message);
            addMemberForm.classList.add('hidden');
        } else {
            alert(result.error);
        }
    });
});