// $$('.bbswrite-save').on('click', function(){
//   alert(1);
//   var formData = app.form.convertToData('#form-bbs-save');
//   alert(formData);
// });

<<<<<<< HEAD
function fBbs_Save_Add () {
=======
function fBbsWriteSave () {
>>>>>>> b9c8b78407c419119e26f63d73d4148dd5e419ba
  var formData = app.form.convertToData('#form-bbs-save');
	console.log (formData);
	if (formData.category == '') {
		app.dialog.alert ('카테로기명을 입력하세요.', '입력오류');
	} else if (formData.word == '') {
		app.dialog.alert ('단어를 입력하세요.', '입력오류');
	} else {
<<<<<<< HEAD
    app.request.post ('/bbs_save_add', formData, function (data) {
=======
    app.request.post ('/bbs_insert', formData, function (data) {
>>>>>>> b9c8b78407c419119e26f63d73d4148dd5e419ba
      console.log(data);
      discoverView.router.back({force : true, ignoreCache : true, reload : true});
    });

    // app.request.post ('/bbs/insert', formData, function (data) {	
		// 	msg = JSON.parse (data);
		// 	if (msg.success) {
    //     fntoastTop ('gg');
    //     app.router.navigate('/bbs/list', {reloadCurrent:true})
    //     //app.router.back ({force : true, ignoreCache : true, reload : true});
		// 	} else if (! msg.success) {
		// 		app.dialog.alert (msg.failMsg, '저장오류');
		// 	} else {
		// 		app.dialog.alert ('예상치 않은 오류가 발생했습니다.', '기타오류');
		// 	}
		// });
	}
}