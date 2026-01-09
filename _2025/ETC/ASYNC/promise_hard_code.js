function delay_word(word, delay) {
	return new Promise(resolve => {
		setTimeout(function () {
			resolve(word)
		}, delay)
	})
}

delay_word('SAMSUNG', 500).then((resolve) => {
	console.log(resolve)
	delay_word('SW', 490).then((resolve) => {
		console.log(resolve)
		delay_word('ACADEMY', 480).then((resolve) => {
			console.log(resolve)
			delay_word('FOR', 470).then((resolve) => {
				console.log(resolve)
				delay_word('YOUTH', 460).then((resolve) => {
					console.log(resolve)
				})
			})
		})
	})
})
