const roleRadios = document.querySelectorAll('input[name="role"]');
const startupFields = document.getElementById('startupFields');
const mentorFields = document.getElementById('mentorFields');
const investorFields = document.getElementById('investorFields');

roleRadios.forEach(radio => {
    radio.addEventListener('change', () => {
        // Hide all role fields
        startupFields.style.display = 'none';
        mentorFields.style.display = 'none';
        investorFields.style.display = 'none';

        // Show only selected role fields
        if(radio.value === 'startup') startupFields.style.display = 'block';
        else if(radio.value === 'mentor') mentorFields.style.display = 'block';
        else if(radio.value === 'investor') investorFields.style.display = 'block';
    });
});