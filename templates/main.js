
const submit = async () => {
    const code = document.getElementById("code")
    const result = await window.pywebview.api.compile(code.value)

    document.getElementById("result").innerText = result
}