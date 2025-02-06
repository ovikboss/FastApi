function exit(){
    sessionStorage.removeItem('isLoggedIn');
    sessionStorage.removeItem('username');
    // Или для очистки всего:
    sessionStorage.clear();
    window.location.href = 'getbooks.html';
}
