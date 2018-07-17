define(
  ['jquery', 'underscore', 'backbone', 'ErrorPrompt', 'common/fpti-publisher', 'common/utils', 'serialize'],
  function($, _, Backbone, EP, Analytics, commonUtils) {
    'use strict';

    commonUtils.handleToggelMobileMenu();

    var View = Backbone.View.extend({
      el: $('#contactView'),
      pgrp: 'main:restcenternodeweb:::contact-seller',
      checkedboxBuyerPledge: 'AcceptAbusePledge',
      showBuyerPledge: 'BuyerPledgeWhitelisted',

      events: {
        'click input[name=disputeType]': 'showPanel',
        'click input[name=itemCategoryForINR]': 'showItemCategoryContent',
        'click input[name=itemCategoryForSNAD]': 'showItemCategoryContent',
        'click input[name=buyerPurchasedUrl]': 'placeHttpText',
        'blur input[name=buyerPurchasedUrl]': 'removeHttpText',
        'keypress textarea': 'removeErrorStyle',
        'keypress input[type=text]': 'removeErrorStyle',
        'click input[name=itemDescription]': 'removeErrorStyle',
        'focus .hasContextError': 'showError',
        'blur .hasContextError': 'hideError',
        'submit #contactForm': 'checkRefund',
        'change input:radio[name*="item["]': 'prepareNad',
        'change input:checkbox[class="itemselector"]': 'selectItemforDispute',
        'click #buyerPledge': 'clearAlert'
      },

      clearAlert: function() {
        $('.buyerPledgeCheckbox').removeClass('hasError');
      },

      initialize: function() {
        this.inrPanel = $('#inrPanel');
        this.snadPanel = $('#snadPanel');
        this.refundRequestAmount = $('#refundRequestAmount');
        // Popover for purchase protection Text while we clicking product or service
        $('.loadPopover').html($('#hiddenContent').html());
        $('.loadPopover').on('mouseover', function(e) {
          $(e.target).popover('show'); // TODO: this may be undesired
        });
        $('#contactView').on('click', function(e) {
          $('.popover').hide();
        });
        var mipsPanel = $('#mipsPanel');

        if ($.contains(document.documentElement, mipsPanel[0])) {
          if ($('#items').val()) {
            var mipsItems = JSON.parse($('#items').val());
            var mipskeys = Object.keys(mipsItems);
            $.each(mipskeys, function(key, val) {
              var cursel = mipsItems[val];
              $('#item-' + val + '-' + cursel).attr('checked', true);
              $('#check-' + val).prop('checked', true);
            });
          }
          var selectedDispute = $('#mipsDispute')
            .val()
            .split(',');
          if (selectedDispute.indexOf('snad') >= 0) {
            $('.mipsReason').css({ display: '' });
          }
        }

        if ($('#buyerPledge').length > 0) {
          var oParams = {
            pgrp: this.pgrp,
            page: this.showBuyerPledge
          };
          Analytics.recordImpression(oParams);
        }
      },

      removeErrorStyle: function(e) {
        $(e.target)
          .parents('.has-error')
          .removeClass('has-error');
      },

      /**
       * Handles presentation of selected dispute type panel
       * @param {Object} e Event target
       */
      showPanel: function(e) {
        var panel = $(e.target).val();

        if (panel === 'inr') {
          this.inrPanel.removeClass('hide');
          this.inrPanel.find(':input').removeAttr('disabled');
          this.snadPanel.addClass('hide');
          this.snadPanel.find(':input').attr('disabled', 'disabled');
        } else if (panel === 'snad') {
          this.snadPanel.removeClass('hide');
          this.snadPanel.find(':input').removeAttr('disabled');
          this.inrPanel.addClass('hide');
          this.inrPanel.find(':input').attr('disabled', 'disabled');
        }

        return;
      },

      showError: function(event) {
        var id = event.target.id;
        $(event.target).removeClass('errorImage');
        var classList = $('#' + id)
          .attr('class')
          .split(' ');
        $.each(classList, function(index, item) {
          if (item === 'hasContextError') {
            EP.promptError('#' + id, $('#' + id + 'ErrorMessage').text());
          }
        });
      },

      hideError: function(event) {
        var id = event.target.id;
        var textVal = $(event.target).val();
        if (!textVal || textVal.trim().length === 0) {
          if (!$(event.target).hasClass('isOptional')) {
            $(event.target).addClass('errorImage');
          }
        }
        id = id + 'formError';

        $('.' + id).addClass('hide');
      },

      /**
       * Handles presentation of item category content
       * @param {Object} e Event target
       */
      showItemCategoryContent: function(e) {
        var itemCategory = $(e.target).val(),
          missingPartsText,
          inCompleteText;

        $(e.target)
          .parents('.item-category')
          .find('p.alert')
          .addClass('hide')
          .removeClass('show');
        $(e.target)
          .parents('.item-category')
          .find('.' + itemCategory + '-content')
          .removeClass('hide');
        $(e.target)
          .parents('.has-error')
          .removeClass('has-error');

        // Change of name of label 'Missing parts' to 'Incomplete' when the buyer selects 'Services' category
        if (e.target.id === 'serviceSNAD' || e.target.id === 'productSNAD') {
          missingPartsText = $('input[name=missingPartsText]').val();
          inCompleteText = $('input[name=inCompleteText]').val();

          if (e.target.id === 'serviceSNAD') {
            $('#inCompleteLabel').html(inCompleteText);
            $('input[id=missingParts]').val('inComplete');
          } else {
            $('#inCompleteLabel').html(missingPartsText);
            $('input[id=missingParts]').val('missingParts');
          }
        }
      },

      placeHttpText: function(e) {
        var input = $(e.target);

        if (input.val() === '') {
          input.val('http://');
        }
        input.focus();
      },

      removeHttpText: function(e) {
        var input = $('input[name=buyerPurchasedUrl]');
        if (input.val() === 'http://') {
          input.val('');
        }
      },
      showLoader: function() {
        var $body = $('#content');
        var height = $body.css('height');
        $body.append('<div class="loadingCase loading" style="height:' + height + '"></div>');
      },
      hideLoader: function() {
        var $body = $('#content');
        $body.find('.loading').remove();
      },

      checkRefund: function(e) {
        this.showLoader();

        var $form = $(e.target);
        if ($form.data('submitted') === true) {
          return e.preventDefault();
        } else {
          $form.data('submitted', true);
        }

        var data = $('#contactForm').serializeJSON();

        var refundRequestAmount = $('#refundRequestAmount');
        if ($.contains(document.documentElement, refundRequestAmount[0])) {
          var value = refundRequestAmount.val();
          refundRequestAmount.val(value);
          
        } // else{alert("Dom is NA"); return true; 	}
        var mipsPanel = $('#mipsPanel');
        if ($.contains(document.documentElement, mipsPanel[0])) {
          if (data.item === undefined || data.item === null) {
            $('.item-selection').addClass('has-error');
            return false;
          } else {
            $('#items').val(JSON.stringify(data.item));
            $('.item-selection').removeClass('has-error');
          }
        }
        //Check added to validate if Buyer Pledge Checkbox is selected
        if ($('#buyerPledge').length > 0 && !$('#buyerPledge').is(':checked')) {
          $('.buyerPledgeCheckbox').addClass('hasError');
          return false;
        } else {
          //
          if ($('#buyerPledge').length > 0 && $('#buyerPledge').is(':checked')) {
            var oParams = {
              pgrp: this.pgrp,
              link: this.checkedboxBuyerPledge
            };
            Analytics.recordClick(oParams);
          }
        }
        //
      },
      prepareNad: function(e) {
        this.updatemipsSelecton();
        $(e.target)
          .closest('.itemgroup')
          .find('input:checkbox')
          .prop('checked', true);
      },
      updatemipsSelecton: function() {
        var selectedDisputes = [];
        $("input:radio[name*='item[']:checked").each(function() {
          if (selectedDisputes.indexOf($(this).val()) > -1) {
            //Already listed in array
          } else {
            selectedDisputes.push($(this).val());
          }
          $('#mipsDispute').val(selectedDisputes.toString());
          if (selectedDisputes.indexOf('snad', selectedDisputes) < 0) {
            $('.mipsReason').css({ display: 'none' });
          } else {
            $('.mipsReason').css({ display: '' });
          }
        });
      },
      selectItemforDispute: function(e) {
        if (!$(e.target).is(':checked')) {
          $(e.target)
            .closest('.itemgroup')
            .find('input:radio')
            .removeAttr('checked');
          this.updatemipsSelecton();
        } else {
          $(e.target)
            .closest('.itemgroup')
            .find('input:radio:eq(0)')
            .prop('checked', true);
          this.updatemipsSelecton();
        }
      }
    });

    return View;
  }
);
