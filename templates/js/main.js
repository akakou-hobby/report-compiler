const code = new EasyMDE({
    element: document.getElementById("code"),
    autoDownloadFontAwesome: true,
});

const submit = async () => {
    const result = await window.pywebview.api.compile(code.value())

    document.getElementById("result").innerText = result
}