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
        addCoverLetterElement();

}

function removeAllRemovables() {
    var removable = document.getElementsByClassName("removable");
    while (removable.length != 0) {
        removable[0].parentNode.removeChild(removable[0])
    }
}

function addEmailElement() {
    var container = document.getElementById("filter-container");
    var row = document.createElement("div");
    row.classList.add("row");
    row.classList.add("removable");
    var formGroup = document.createElement("div")
    formGroup.classList.add("form-group");
    var label = document.createElement("label");
    label.innerHTML = "Key points";
    var text = document.createElement("textarea");
    text.classList.add("form-control");
    text.rows = 3;
    text.id = "keyPoints";
    text.name = "keyPoints"
    formGroup.appendChild(label);
    formGroup.appendChild(text);
    row.appendChild(formGroup);
    container.appendChild(row);
}

function addSMSElement() {
    var container = document.getElementById("filter-container");
    var row = document.createElement("div");
    row.classList.add("row");
    row.classList.add("removable");
    var formGroup = document.createElement("div")
    formGroup.classList.add("form-group");
    var label = document.createElement("label");
    label.innerHTML = "Context";
    var text = document.createElement("textarea");
    text.classList.add("form-control");
    text.id = "context";
    text.name = "context";

    formGroup.appendChild(label);
    formGroup.appendChild(text);
    row.appendChild(formGroup);
    container.appendChild(row);
}

function addSongElement() {
    var container = document.getElementById("filter-container");
    var row = document.createElement("div");
    row.classList.add("row");
    row.classList.add("removable");
    var formGroup = document.createElement("div")
    formGroup.classList.add("form-group");
    var label = document.createElement("label");
    label.innerHTML = "Song idea";
    var text = document.createElement("textarea");
    text.classList.add("form-control");
    text.id = "idea";
    text.name = "idea";

    formGroup.appendChild(label);
    formGroup.appendChild(text);
    row.appendChild(formGroup);
    container.appendChild(row);
}

function addStoryElement() {
    var container = document.getElementById("filter-container");
    var row = document.createElement("div");
    row.classList.add("row");
    row.classList.add("removable");
    var formGroup = document.createElement("div")
    formGroup.classList.add("form-group");
    var label = document.createElement("label");
    label.innerHTML = "Story idea";
    var text = document.createElement("textarea");
    text.classList.add("form-control");
    text.id = "idea";
    text.name = "idea";

    formGroup.appendChild(label);
    formGroup.appendChild(text);
    row.appendChild(formGroup);
    container.appendChild(row);
}

function addFacebookElement() {
    var container = document.getElementById("filter-container");
    var row1 = document.createElement("div");
    row1.classList.add("row");
    row1.classList.add("removable");
    var formGroup1 = document.createElement("div")
    formGroup1.classList.add("form-group");
    var label1 = document.createElement("label");
    label1.innerHTML = "Product name";
    var text = document.createElement("input");
    text.classList.add("form-control");
    text.type = "text";
    text.id = "productName";
    text.name = "productName";
    formGroup1.appendChild(label1);
    formGroup1.appendChild(text);
    row1.appendChild(formGroup1);

    var row2 = document.createElement("div");
    row2.classList.add("row");
    row2.classList.add("removable");
    var formGroup2 = document.createElement("div")
    formGroup2.classList.add("form-group");
    var label2 = document.createElement("label");
    label2.innerHTML = "Product description";
    var description = document.createElement("textarea");
    description.classList.add("form-control");
    description.id = "productDescription";
    description.name = "productDescription";

    formGroup2.appendChild(label2);
    formGroup2.appendChild(description);
    row2.appendChild(formGroup2);

    container.appendChild(row1);
    container.appendChild(row2);
}

function addCoverLetterElement() {
    var container = document.getElementById("filter-container");
    var row1 = document.createElement("div");
    row1.classList.add("row");
    row1.classList.add("removable");
    var formGroup1 = document.createElement("div")
    formGroup1.classList.add("form-group");
    var label1 = document.createElement("label");
    label1.innerHTML = "Job Role";
    var text1 = document.createElement("input");
    text1.classList.add("form-control");
    text1.type = "text";
    text1.id = "jobRole";
    text1.name = "jobRole";
    formGroup1.appendChild(label1);
    formGroup1.appendChild(text1);
    row1.appendChild(formGroup1);

    var row2 = document.createElement("div");
    row2.classList.add("row");
    row2.classList.add("removable");
    var formGroup2 = document.createElement("div")
    formGroup2.classList.add("form-group");
    var label2 = document.createElement("label");
    label2.innerHTML = "Job Skills";
    var text2 = document.createElement("input");
    text2.classList.add("form-control");
    text2.type = "text";
    text2.id = "jobSkills";
    text2.name = "jobSkills";
    formGroup2.appendChild(label2);
    formGroup2.appendChild(text2);
    row2.appendChild(formGroup2);

    container.appendChild(row1);
    container.appendChild(row2);
}