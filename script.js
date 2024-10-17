function generatePassword() {
    const letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
    const numbers = '0123456789'.split('');
    const symbols = '!#$%&()*+'.split('');

    const nrLetters = parseInt(document.getElementById('letters').value);
    const nrSymbols = parseInt(document.getElementById('symbols').value);
    const nrNumbers = parseInt(document.getElementById('numbers').value);

    // Generate Easy Level Password
    let passwordEasy = [];

    for (let i = 0; i < nrLetters; i++) {
        passwordEasy.push(letters[Math.floor(Math.random() * letters.length)]);
    }

    for (let i = 0; i < nrSymbols; i++) {
        passwordEasy.push(symbols[Math.floor(Math.random() * symbols.length)]);
    }

    for (let i = 0; i < nrNumbers; i++) {
        passwordEasy.push(numbers[Math.floor(Math.random() * numbers.length)]);
    }

    const easyPassword = passwordEasy.join('');
    document.getElementById('easyPassword').innerText = easyPassword;

    // Generate Hard Level Password (Shuffle characters)
    let passwordHard = passwordEasy.slice(); // Clone array
    passwordHard.sort(() => 0.5 - Math.random());

    const hardPassword = passwordHard.join('');
    document.getElementById('hardPassword').innerText = hardPassword;
}
