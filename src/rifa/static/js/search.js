

var vueProducts =
    new Vue({
        delimiters: ['[[', ']]'],
        el: '#products-list',
        data () {
            return {
              list_result: null,
              columns: ['', 'Product', 'Brand', 'Category', 'Scoring Date', 'Index', 'Index details'],
              loading: true,
              errored: false
            }
        },
        methods: {
            searchProducts: function() {

                var searchVal = $('#my_search_input').val();
                if(searchVal.length >= 0) {
                    axios.get('/products/?search=' + searchVal)
                      .then(response => {
                        this.list_result = response.data.results;
                      })
                      .catch(error => {
                        console.log(error)
                        this.errored = true
                      })
                      .finally(() => this.loading = false);
                  }
                },
                listProducts: function () {
                    this.searchProducts();
                },
                getImgUrl: function(tableSrc) {
                    if(tableSrc && tableSrc.length > 0) {
                        return tableSrc[0];
                    }
                    return 'https://cdn.iconscout.com/icon/free/png-256/smartphone-1703329-1446727.png'
                },
                gotoScoringLink: function (scoringLink) {
                    if(scoringLink) {
                        window.open(scoringLink, '_blank');
                    }
                    window.open('https://www.ecologie.gouv.fr/indice-reparabilite', '_blank');
                },
                displayScore: function (score) {
                    var path = "/static/assets/score/";
                    if(score && score > 0) {
                        return path + "logo-indice-" + score + ".png";
                    }
                    return path + "logo-indice-default.png";
                }
            },
            mounted () {
                this.listProducts();
            }
    });