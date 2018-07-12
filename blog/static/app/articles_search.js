let url = window.location.origin + "/articles/search?query=";

function searchArticles(input) {
    setTimeout(() => {
        fetch(url+input.value).then(function(response) {
            return response.json();
        })
        .then(function(response) {
            serveResults(response);
        });
    }, 300);
}

function serveResults(response) {
    // hide regular content, reset animation class
    let articleList = document.createElement("article-list");
    let contentArea = document.querySelector("content-area");
    while (contentArea.firstChild) {
        contentArea.removeChild(contentArea.firstChild);
    }
    contentArea.classList.remove("search_result_blink");

    // prepare results for injection
    match = false
    response.articles.forEach((article) => {
        match = true
        tags = []
        article.tags.forEach((tag) => {
            tags.push(`<tag>${tag}</tag>`)
        });
        articleList.insertAdjacentHTML('afterbegin',
        `<article>
            <a href="${article.url}"><info><span class="timestamp" datetime="${article.updated}"></span>${tags}</info>
            <h1>${article.headline}</h1></a>
        </article>`
    );
    })
    
    // inject results, start timeago.js and add highlighting animation
    contentArea.appendChild(articleList);
    timeago(null, 'de').render(document.querySelectorAll(".timestamp"));
    if (match) {
        setTimeout(() => {
            contentArea.classList.add("search_result_blink");
        }, 20);
    }
}