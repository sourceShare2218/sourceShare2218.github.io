function changePage(number) {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.status == 200) {
            let content = JSON.parse(this.content);
            console.log(content);
            document.getElementById("lecture-frame").src = content;
        }
    };
    xhttp.open("GET", `https://raw.githubusercontent.com/sourceShare2218/IntroductionToAlgorithm/master/Day${number}.html`, true);
    xhttp.send();
}