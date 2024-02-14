let likes = [9, 16, 13];


// function to add likes 
function addLike(i) {
    likes[i]++;
    let num = document.querySelector('.num' + i);
    num.innerHTML = likes[i];
}