from django import forms
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe


class StarRatingWidget(forms.TextInput):

    def render(self, name, value, attrs=None):
        super(StarRatingWidget, self).render(name, value, attrs)
        if  not attrs:
            attrs = {}
        flat_attrs = flatatt(attrs)
        html = """
        <input %(attrs)s name="%(name)s" type="hidden" value="%(value)s" required="false"/>
        <div id="_%(name)s"></div>
        <script>
        (function($){
            $(function(){
                var $stars = $("#_%(name)s");
                $stars.starRating({
                    starSize: 40,
                    starShape: 'rounded',
                    useFullStars: true,
                    disableAfterRate: false,
                    callback: function(currentRating, $el){
                        var rating = $stars.starRating('getRating');
                        $stars.prev('input').val(rating);
                    }
                });

                // if not filled in default to zero.
                var old_rating = $stars.prev('input').val();

                if (old_rating == 'None'){
                    $stars.prev('input').val(0);
                }
            });
        })(jQuery);
        </script>
        """ % {'attrs': flat_attrs,
               'value': value,
               'name': name,
              }

        return mark_safe(html)
