function initPasteDragImg(Editor){
    var doc = document.getElementById(Editor.id);
    doc.addEventListener('paste', function (event) {

        console.log(event);
        var items = (event.clipboardData || window.clipboardData).items;
        console.log(event.clipboardData);
        var file = null;
        if (items && items.length) {

            // 搜索剪切板items
            for (var i = 0; i < items.length; i++) {
                if (items[i].type.indexOf('image') !== -1) {
                    file = items[i].getAsFile();
                    break;
                }
            }
        } else {
            console.log("当前浏览器不支持");
            return;
        }
        if (!file) {
            console.log("粘贴内容非图片");
            return;
        }
        uploadImg(file,Editor);
    });
    var dashboard = document.getElementById(Editor.id);
    dashboard.addEventListener("dragover", function (e) {
        e.preventDefault();
        e.stopPropagation();
    });
    dashboard.addEventListener("dragenter", function (e) {
        e.preventDefault();
        e.stopPropagation();
    });
    dashboard.addEventListener("drop", function (e) {
        e.preventDefault();
        e.stopPropagation();
     var files = this.files || e.dataTransfer.files;
     uploadImg(files[0],Editor);
     })
}
function uploadImg(file,Editor){
    var formData = new FormData();
    var fileName=file.name;
    console.log(file);
    formData.append('editormd-image-file', file, fileName);

    $.ajax({
        url: Editor.settings.imageUploadURL,
        type: 'post',
        data: formData,
        processData: false,
        contentType: false,
        dataType: 'json',
        success: function (msg) {
            // console.log(msg);
            var success = msg['success'];
            if(success==1){
                var url = msg["url"];
                if(/\.(png|jpg|jpeg|gif|bmp|ico)$/.test(url)){

                    Editor.replaceSelection('![图片alt]('+msg["url"]+')');
                    console.log("![图片alt]("+msg["url"]+")")
                }else{
                    Editor.replaceSelection("[下载附件]("+msg["url"]+")");
                }
            }else{
                console.log(msg);
                alert("上传失败");
            }
        }
    });


}

$(function () {
    editormd("id_content-wmd-wrapper", {
            watch: false, // 关闭实时预览
            lineNumbers: false,
            lineWrapping: false,
            width: "1200",
            height: 500,
            placeholder: '',
            // 当有多个mdeditor时，全屏后，其他mdeditor仍然显示，解决此问题。
            onfullscreen : function() {
                this.editor.css("border-radius", 0).css("z-index", 9999);
            },
            onfullscreenExit : function() {
                this.editor.css({
                    zIndex : 10,
                    border : "1px solid rgb(221,221,221)"
                })
            },
            syncScrolling: "single",
            path: "/static/mdeditor/js/lib/",
            // theme
            theme : "default",
            previewTheme : "default",
            editorTheme : "default",

            saveHTMLToTextarea: true, // editor.md 有问题没有测试成功
            toolbarAutoFixed: true,
            searchReplace: true,
            emoji: true,
            tex: true,
            taskList: false,
            flowChart: true,
            sequenceDiagram: true,

            // image upload
            imageUpload: true,
            imageFormats: ['jpg', 'jpeg', 'gif', 'png', 'bmp', 'webp'],
            imageUploadURL: "/mdeditor/uploads/",
            toolbarIcons: function () {
                return ['undo', 'redo', '|', 'bold', 'del', 'italic', 'quote', 'ucwords', 'uppercase', 'lowercase', '|', 'h1', 'h2', 'h3', 'h5', 'h6', '|', 'list-ul', 'list-ol', 'hr', '|', 'link', 'reference-link', 'image', 'code', 'preformatted-text', 'code-block', 'table', 'datetime', 'emoji', 'html-entities', 'pagebreak', 'goto-line', '|', 'help', 'info', '||', 'preview', 'watch', 'fullscreen']
            },
            onload: function () {
                // console.log('onload', this);
                initPasteDragImg(this);//必须
                //this.fullscreen();
                //this.unwatch();
                //this.watch().fullscreen();

                //this.setMarkdown("#PHP");
                //this.width("100%");
                //this.height(480);
                //this.resize("100%", 640);
            }
        });
});
