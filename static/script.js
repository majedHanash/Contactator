document.onload = handleOnLoad();

function addElements() {
    console.log("hi");
    removeAllRemovables();
    var useCase = document.getElementById("useCase").value;
    if (useCase == "Email")
        addEmailElement();
    else if (useCase == "SMS")
        addSMSElement();
    else if (useCase == "Song")
        addSongElement();
    else if (useCase == "Story")
        addStoryElement();
    else if (useCase == "Facebook")
        addFacebookElement();
    else if (useCase == "CoverLetter")
        addCoverLetterElements();
    else if (useCase == "VideoChannelDescription")
        addVideoChannelDescriptionElements();
    else if (useCase == "BlogIdea")
        addBlogIdeaElement();
    else if (useCase == "InterviewQuestions")
        addInterviewQuestionsElements();
    else if (useCase == "JobDescription")
        addJobDescriptionElement();
    else if (useCase == "Tagline")
        addTaglineElement();
    else if (useCase == "Testimonial")
        addTestimonialElements();


}

function removeAllRemovables() {
    var removable = document.getElementsByClassName("removable");
    while (removable.length != 0) {
        removable[0].parentNode.removeChild(removable[0])
    }
}

function addEmailElement() {
    var container = document.getElementById("filter-container");
    var row = addLabeledTextareaElement("Key points", "keyPoints", "keyPoints", 3);
    container.appendChild(row);
}

function addSMSElement() {
    var container = document.getElementById("filter-container");
    var row = addLabeledTextareaElement("Context", "context", "context");
    container.appendChild(row);
}

function addSongElement() {
    var container = document.getElementById("filter-container");
    var row = addLabeledTextareaElement("Song idea", "idea", "idea");
    container.appendChild(row);
}

function addStoryElement() {
    var container = document.getElementById("filter-container");
    var row = addLabeledTextareaElement("Story idea", "idea", "idea");
    container.appendChild(row);
}

function addFacebookElement() {
    var container = document.getElementById("filter-container");
    var row1 = addLabeledTextElement("Product name", "productName", "productName");

    var row2 = addLabeledTextareaElement("Product description", "productDescription", "productDescription");
    container.appendChild(row1);
    container.appendChild(row2);
}

function addCoverLetterElements() {
    var container = document.getElementById("filter-container");
    var row1 = addLabeledTextElement("Job Role", "jobRole", "jobRole");
    var row2 = addLabeledTextElement("Job Skills", "jobSkills", "jobSkills");

    container.appendChild(row1);
    container.appendChild(row2);
}

function addVideoChannelDescriptionElements() {
    var container = document.getElementById("filter-container");
    var row1 = addLabeledTextElement("Category", "category", "category");
    var row2 = addLabeledTextElement("Channel name", "name", "name");
    var row3 = addLabeledTextElement("What to cover", "cover", "cover");

    container.appendChild(row1);
    container.appendChild(row2);
    container.appendChild(row3);
}

function addBlogIdeaElement() {
    var container = document.getElementById("filter-container");
    var row = addLabeledTextElement("Primary keyword", "primaryKeyword", "primaryKeyword");
    container.appendChild(row);
}

function addInterviewQuestionsElements() {
    var container = document.getElementById("filter-container");
    var row1 = addLabeledTextareaElement("Interviewee bio", "intervieweeBio", "intervieweeBio", 3);
    var row2 = addLabeledTextareaElement("Interview context", "interviweContext", "interviewContext");
    container.appendChild(row1);
    container.appendChild(row2);
}

function addJobDescriptionElement() {
    var container = document.getElementById("filter-container");
    var row = addLabeledTextElement("Jobe role", "role", "role");
    container.appendChild(row);
}

function addTaglineElement() {
    var container = document.getElementById("filter-container");
    var row = addLabeledTextareaElement("Description", "description", "description", 3);
    container.appendChild(row);
}

function addTestimonialElements() {
    var container = document.getElementById("filter-container");
    var row1 = addLabeledTextElement("Name", "name", "name");
    var row2 = addLabeledTextareaElement("Review title", "reviewTitle", "reviewTitle");
    container.appendChild(row1);
    container.appendChild(row2);
}


function addLabeledTextElement(labelText, id, name) {
    var row = document.createElement("div");
    row.classList.add("row");
    row.classList.add("removable");
    var formGroup = document.createElement("div")
    formGroup.classList.add("form-group");
    var label = document.createElement("label");
    label.innerHTML = labelText;
    var text = document.createElement("input");
    text.classList.add("form-control");
    text.type = "text";
    text.id = id;
    text.name = name;
    formGroup.appendChild(label);
    formGroup.appendChild(text);
    row.appendChild(formGroup);
    return row
}

function addLabeledTextareaElement(labelText, id, name, rows = 2) {
    var row = document.createElement("div");
    row.classList.add("row");
    row.classList.add("removable");
    var formGroup = document.createElement("div")
    formGroup.classList.add("form-group");
    var label = document.createElement("label");
    label.innerHTML = labelText;
    var text = document.createElement("textarea");
    text.classList.add("form-control");
    text.rows = rows;
    text.id = id;
    text.name = name;
    formGroup.appendChild(label);
    formGroup.appendChild(text);
    row.appendChild(formGroup);
    return row;
}

