$(function () {
  $('#target-date').datepicker()
  $('#feature-search').change(function () {
    if ($(this).val() === 'client') {
      $('#search-helper').html('')
      $('#search-helper')
        .html(`<select class="form-control" id="client">
          <option value="clientA">Client A</option>
          <option value="clientB">Client B</option>
          <option value="clientC">Client C</option>
        </select>`)
      $('#target-date').hide()
    } else if ($(this).val() === 'date') {
      $('#search-helper').html('')
      $('#target-date').show()
    } else {
      $('#search-helper').html('')
      $('#search-helper')
        .html(`<select class="form-control" id="product-areas">
          <option value="policies">Policies</option>
          <option value="claims">Claims</option>
          <option value="billing">Billing</option>
          <option value="reports">Reports</option>
        </select>`)
      $('#target-date').hide()
    }
  })

  $('#search-btn').on('click', function (e) {
    let featureSearch = $('#feature-search')
    let selection

    switch (featureSearch.val()) {
      case 'date':
        selection = $('#target-date').val()
        break
      case 'client':
        selection = $('#client').val()
        break
      case 'product-areas':
        selection = $('#product-areas').val()
        break
      default:
        break
    }
    const dataBuilder = `query=${featureSearch.val()}:${selection}`
    return $.ajax({
      url: '/search',
      method: 'post',
      data: dataBuilder,
      success: function (response) {
        let tbody = $('#feature-table tbody')
        if (response.length > 0) {
          let html = ''
          tbody.empty()
          $.each(response, function (key, value) {
            html += `
                <tr><td>${key + 1}</td>
                    <td>${value.title}</td>
                    <td>${value.description}</td>
                    <td>${value.client}</td>
                    <td>${value.client_priority}</td>
                    <td>${value.target_date}</td>
                    <td>${value.product_areas}</td>
                </tr>`
          })
          tbody.html(html)
          // feature_table.html(html)
        } else {
          tbody.empty()
        }
      },
      error: function (err) {
        console.log(err)
      }
    })
  })
})
