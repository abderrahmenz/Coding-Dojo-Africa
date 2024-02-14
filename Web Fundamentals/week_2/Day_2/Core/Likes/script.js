
let likes = [13];

function addLike(i) {
    likes[i]++;
    let like = document.querySelector('.like' +i);
    like.innerHTML = likes[i];
}