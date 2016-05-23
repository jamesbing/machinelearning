


<script>
      function oneClickSubmit(button, waitingText) {
          button.disabled = true;
          var $button = $(button);
          $button.html('<i class="icon-spinner icon-spin"></i> ' + waitingText);
          $button.closest('form').submit();
          return true;
      }
    </script>








<!DOCTYPE html>

<html>
    


<head>
    <title>LeJit/GPU_Example - Domino</title>
    <meta charset="utf-8">


    <meta name="google" content="notranslate">
    <meta property="og:image" content="/assets/images/domino_logo.png">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" type="image/png" href="/assets/images/favicon.png?v3">

    
    
        <script src="//cdn.optimizely.com/js/2853210246.js"></script>
    


    
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js" type="text/javascript"></script>
        <!--<script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.0/jquery-ui.min.js" type="text/javascript"></script>-->

        <script src="/assets/thirdparty/bootstrap/js/bootstrap.min.js" type="text/javascript"></script>
    

    <script src="/assets/javascripts/domino.js" type="text/javascript"></script>
    <script src="/assets/thirdparty/jquery.noty.packaged.min.js" type="text/javascript"></script>
    <script src="/assets/javascripts/common/util/userAlert.js" type="text/javascript"></script>
    <script src="/assets/thirdparty/moment.min.js" type="text/javascript"></script>

    <!-- select2 -->
    <script src="/assets/thirdparty/select2.full.min.js" type="text/javascript"></script>
    <link rel="stylesheet" media="all" href="/assets/thirdparty/select2.min.css">

    <!-- Replace Bootstrap with Flatly -->
    <link rel="stylesheet" media="screen" href="/assets/thirdparty/bootstrap/css/bootstrap.min.css">
    

    <!-- typeahead extra -->
    <script src="/assets/thirdparty/typeahead.min.js" type="text/javascript"></script>
    <link rel="stylesheet" media="all" href="/assets/thirdparty/typeahead-bootstrap.css">


    <link rel="stylesheet" media="all" href="/assets/thirdparty/jquery.atwho.min.css">
    <script src="/assets/thirdparty/jquery.caret.min.js" type="text/javascript"></script>
    <script src="/assets/thirdparty/jquery.atwho.min.js" type="text/javascript"></script>

    <link rel="stylesheet" media="all" href="/assets/thirdparty/font-awesome/css/font-awesome.css">
    <link rel="stylesheet" media="all" href="/assets/thirdparty/ss-gizmo/ss-gizmo.css">
    <link rel="stylesheet" media="all" href="/assets/stylesheets/sass-bootstrap-domino.min.css">
    <link rel="stylesheet" media="all" href="/assets/stylesheets/webapp.css">
    <link href='//fonts.googleapis.com/css?family=Lato:300,400,700' rel='stylesheet' type='text/css'>

    <!-- google code prettify -->
    <link rel="stylesheet" media="all" href="/assets/thirdparty/google-code-prettify/prettify.css">


    
    <script>
    
        var thirdPartyRoot = '/assets/thirdparty/';

        var require = {
            shim: {
                'underscore': {
                    exports: '_'
                },
                'backbone': {
                    deps: ['underscore'],
                    exports: 'Backbone'
                },
                'remaining' : {
                    exports: 'remaining'
                },
                'backbone_paginator': {
                    deps: ['backbone', 'underscore'],
                    exports: 'Backbone.Paginator'
                },
                'backgrid' : {
                    deps: ['backbone', 'underscore'],
                    exports: 'Backgrid'
                } ,
                'backgrid_filter' : {
                    deps: ['backgrid', 'lunr'],
                    exports: 'BackgridFilter'
                },
                'noty' : {
                    exports: 'noty'
                },
                'validator' : {
                    exports: 'validator'
                },
                'userAlert' : {
                    exports: 'UserAlert'
                },
                'highcharts': {
                    exports: 'Highcharts'
                }
            },

            baseUrl: '/assets/javascripts',

            paths: {
                common:             '/assets/javascripts/common',
                thirdparty :        thirdPartyRoot,
                backstretch:        thirdPartyRoot + 'jquery.backstretch.min',
                backgrid:           thirdPartyRoot + 'backgrid/backgrid.min',
                backgrid_filter:    thirdPartyRoot + 'backgrid/extensions/filter/backgrid-filter',
                lunr:               thirdPartyRoot + 'lunr.min',
                underscore:         thirdPartyRoot + 'underscore.min',
                backbone:           thirdPartyRoot + 'backbone-min',
                validator:          thirdPartyRoot + 'bootstrap/js/bootstrap-validator',
                moment:             thirdPartyRoot + 'moment.min',
                remaining:          thirdPartyRoot + 'remaining',
                backbone_paginator: thirdPartyRoot + 'backbone.paginator.min',
                userAlert:          '/assets/javascripts/common/util/userAlert',
                noty:               thirdPartyRoot + 'jquery.noty.packaged.min',
                highcharts:         thirdPartyRoot + 'highcharts'
            }
        };
    
    </script>

    
    
    
    <script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

      ga('create', 'UA-43833030-1', 'auto');

      // send Optimizely data into GA
      window.optimizely = window.optimizely || [];
      window.optimizely.push("activateUniversalAnalytics");

      ga('send', 'pageview');

    </script>
    


        <!-- Suppressing IE11's tile configuration -->
    <meta name="msapplication-config" content="none" />

    
    
        <script type="text/javascript">(function(e,b){if(!b.__SV){var a,f,i,g;window.mixpanel=b;a=e.createElement("script");a.type="text/javascript";a.async=!0;a.src=("https:"===e.location.protocol?"https:":"http:")+'//cdn.mxpnl.com/libs/mixpanel-2.2.min.js';f=e.getElementsByTagName("script")[0];f.parentNode.insertBefore(a,f);b._i=[];b.init=function(a,e,d){function f(b,h){var a=h.split(".");2==a.length&&(b=b[a[0]],h=a[1]);b[h]=function(){b.push([h].concat(Array.prototype.slice.call(arguments,0)))}}var c=b;"undefined"!==
    typeof d?c=b[d]=[]:d="mixpanel";c.people=c.people||[];c.toString=function(b){var a="mixpanel";"mixpanel"!==d&&(a+="."+d);b||(a+=" (stub)");return a};c.people.toString=function(){return c.toString(1)+".people (stub)"};i="disable track track_pageview track_links track_forms register register_once alias unregister identify name_tag set_config people.set people.set_once people.increment people.append people.track_charge people.clear_charges people.delete_user".split(" ");for(g=0;g<i.length;g++)f(c,i[g]);
    b._i.push([a,e,d])};b.__SV=1.2}})(document,window.mixpanel||[]);
    mixpanel.init("a8873acdc08507d2ac6f95399536cc32");


        
            mixpanel.track('Viewed page', {'Page': 'LeJit/GPU_Example'});
        

        </script>
    

    
    
    


    
      
          <script type='text/javascript'>(function() {var walkme = document.createElement('script'); walkme.type = 'text/javascript'; walkme.async = true; walkme.src = '/assets/javascripts/walkme/walkme_274a1297004e4b8aa687bb9b7b3366ff_https.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(walkme, s); window._walkmeConfig = {smartLoad:true};})();</script>
        
    
</head>
















<!-- by putting the message content in its own script tag, we avoid issues that arise when the content has quotation marks  -->


<script type="text/javascript">
/**
* Render timestamps with clients locale.
*/

$(function() {
    window.domino = window.domino || {};

    window.domino.utils = window.domino.utils || {};

    window.domino.utils.defaultTimestampFormat  = window.domino.utils.defaultTimestampFormat  || "MMM DD, YYYY @ hh:mm a";

    window.domino.utils.renderTimestamps = window.domino.utils.renderTimestamps || function renderTimestamps() {
        $(".timestamp").each(function (index, element) {
            var $element = $(element);
            var timestamp = $element.data('millis');

            var format = window.domino.utils.defaultTimestampFormat;

            if ($element.data('format')) {
                format = $element.data('format');
            }

            var renderedTimestamp = moment(timestamp).format(format);
            $element.html(renderedTimestamp);
        });
    }

    window.domino.utils.renderTimestamps();

    window.domino.utils.updateLocationOnTabClicked = window.domino.utils.updateLocationOnTabClicked || function() {
        $('.nav-tabs a').on('shown.bs.tab', function (e) {
            window.location.hash = e.target.hash;
        })
    };

    window.domino.utils.selectNavigationTabFromUrl = window.domino.utils.selectNavigationTabFromUrl || function() {
        var hash = window.location.hash;
        if (hash) {
            $('.nav-tabs a[href$='+ hash +']').tab('show') ;
        }
    }

    window.domino.utils.selectNavigationTabFromUrl();
    window.domino.utils.updateLocationOnTabClicked();

    window.addEventListener("hashchange", window.domino.utils.selectNavigationTabFromUrl, false);
});
</script>


    <!-- This class will add and override bootstrap looks -->
    <body class="domino-webapp">
        
    


<nav class="navbar navbar-default navbar-fixed-top webapp-navbar " role="navigation">

    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="container-fluid">

            <!-- Includes the logo and navigation to the overview page -->
        <div class="navbar-header alt">
            <a class="navbar-logo" href="http://www.dominodatalab.com">
                
                    <img src="/assets/images/logos/webapp-navbar-logo.svg"/>
                
            </a>
        </div>


        <!-- project path + section path + section main action buttons -->
        <div class="no-collapse">

            
                <ul class="show-only-smallscreens nav navbar-nav navbar-left separators-right">
                    <li>
                        <a href="#" data-action="togglesidebar"><i class="glyphicon glyphicon-list"></i></a>
                    </li>
                </ul>
            

            
        
            
    <ul class="nav navbar-nav project-path navbar-left project-path-project">
        <li>
            <a class="path-user" href="/LeJit#projects">
                LeJit/
            </a>
        </li>
        <li class="path-project-container">
            <a title="GPU_Example" class="path-project main-path ellipsis" href="/LeJit/GPU_Example#console">
                GPU_Example
            </a>
        </li>

    </ul>

        
    

            
            <!-- Align the navigation to the right -->
            <ul class="nav navbar-nav navbar-right nav-utility noauth">
                
                  
                
                
                        
                            <li>
                                <a class="btn btn-success btn-sm" href="https://www.dominodatalab.com/trial" class="username">
                                    <span>Sign Up</span>
                                </a>
                            </li>
                        
                        <li>
                            <a target="_blank" href="http://support.dominodatalab.com"><span>Help</span></a>
                        </li>
                        <li>
                            <a class="logout-btn" href="/login"><span>Log In</span></a>
                        </li>
                    
            </ul>
        </div>
    </div>
</nav>




        <!-- Container fluid needs to wrap the webapp -->
        <div class="container-fluid">
            <div>

                <!-- Content of the sidebar, left side of the app -->
                
                <div id="sidebar" class="sidebar">

                    <!-- Top section of the sidebar -->
                    <div id="sidebar-top" class="light-scroll">
                            
    <!--
        nav-sidebar looks
        Bootstrap friendly ✓
    -->
    <ul class="nav nav-sidebar">
        
            
    <li class="  ">
        <i class="icon icon-file-text-alt icon-fixed-width"></i><a href="/LeJit/GPU_Example/overview">Overview</a>
    </li>

        
        
            
    <li class="  ">
        <i class="icon icon-spinner"></i><a href="/LeJit/GPU_Example#console">Runs</a>
    </li>

            
        
        
            
    <li class="  ">
        <i class="icon icon-comments-alt icon-fixed-width"></i><a href="/LeJit/GPU_Example/newsfeed">Discussion</a>
    </li>

        
        
            
    <li class="  ">
        <i class="icon icon-bar-chart icon-fixed-width"></i><a href="/LeJit/GPU_Example/results">Results</a>
    </li>

        
        
        
            
    <li class=" active ">
        <i class="icon ss-gizmo ss-files"></i><a href="/LeJit/GPU_Example/browse/">Files</a>
    </li>

        
        
            
    <li class="  ">
        <i class="icon glyphicon glyphicon-eye-open"></i><a href="/LeJit/GPU_Example/reviews">Reviews</a>
    </li>

        
        
        
            
    <li class="  ">
        <i class="icon glyphicon glyphicon-cog"></i><a href="/LeJit/GPU_Example/settings#execution">Settings</a>
    </li>

            
    <li class="  ">
        <ul class="sub-menu">
            <li><i class="icon icon-sitemap"></i><a href="/LeJit/GPU_Example/dependencies">Imports/Exports</a></li>
        </ul>
    </li>

        
    </ul>

    <div class="separator"></div>

    <ul class="nav nav-sidebar secondary">
        
        <li>
            
                <i class="icon ss-gizmo ss-unlock"></i>
                <a href="/LeJit/GPU_Example/settings#sharing">Project is public</a>
            
        </li>
        

        
            

            
                
                    <li style="padding: 10px 25px">
                    <select onchange="if (this.value) window.location.href=this.value" class="form-control input-sm">
                        <option>Other related forks</option>
                        
                            <option value="/HWU_PVL/GPU_Example#console">HWU_PVL/GPU_Example</option>
                        
                            <option value="/Tim_Domino/GPU_Example#console">Tim_Domino/GPU_Example</option>
                        
                            <option value="/carlosgavina/GPU_Example2#console">carlosgavina/GPU_Example2</option>
                        
                            <option value="/danson/GPU_Example#console">danson/GPU_Example</option>
                        
                            <option value="/deeplearnjp/GPU_Example#console">deeplearnjp/GPU_Example</option>
                        
                            <option value="/fone4u/GPU_Example#console">fone4u/GPU_Example</option>
                        
                            <option value="/obaes/GPU_Example#console">obaes/GPU_Example</option>
                        
                            <option value="/zhvihti/GPU_Example#console">zhvihti/GPU_Example</option>
                        
                    </select>
                    </li>
                
            
        

        
            <li style="padding: 25px;">
                <button class="btn btn-block btn-default" href="#fork-modal" data-toggle="modal" href="#fork">
                    <i class="icon-code-fork"></i> Fork this project</button>
            </li>
        

    </ul>

    <div class="separator"></div>

    <ul class="nav nav-sidebar info status-failed">
        <li>
            
    
         
    

        </li>
    </ul>

                    </div>

                    
    <!-- Bottom part of the sidebar -->
    <ul id="sidebar-bottom" class="sidebar-bottom nav nav-sidebar secondary absolute-bottom secondary-menu">
        <li class="fadearea"></li>
        <li>
            <!--
                Making the links horizontal, overriding the bootstrap default behaviour

                NOT Bootstrap friendly ×
            -->
            <div class="horizontal-links">
                <a target="_blank" href="http://support.dominodatalab.com">Help</a>
                <a target="_blank" href="http://www.dominodatalab.com/about#contact">Contact</a>
                
                    <a target="_blank" href="http://www.dominodatalab.com/careers.html">Careers</a>

                    <!-- This should fire a dropdown menu for the rest of the options -->
                    <div class="dropdown float-right dropup">
                      <a href="#" class="float-right icon glyphicon glyphicon-align-justify" id="dropdownMenu1" data-toggle="dropdown"></a>
                      <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">
                        <li role="presentation"><a target="_blank" role="menuitem" tabindex="-1" href="http://www.dominodatalab.com/privacy.html">Privacy Policy</a></li>
                        <li role="presentation"><a target="_blank" role="menuitem" tabindex="-1" href="http://www.dominodatalab.com/security.html">Security</a></li>
                        <li role="presentation"><a target="_blank" role="menuitem" tabindex="-1" href="http://www.dominodatalab.com/terms.html">Terms of Service</a></li>
                        <li role="presentation" class="divider"></li>
                        <li role="presentation"><a target="_blank" role="menuitem" tabindex="-1" href="http://twitter.com/dominodatalab">Twitter @dominodatalab</a></li>
                      </ul>
                    </div>
                

            </div>

        </li>

    </ul>

                </div>
                

                <!-- The content of each section is inside this area -->
                
                
                    <div class="main do-list-detail">
                
                    
                        
    
    <script src="/assets/thirdparty/google-code-prettify/prettify.js"></script><script src="/assets/thirdparty/google-code-prettify/lang-matlab.js"></script><script src="/assets/thirdparty/google-code-prettify/lang-r.js"></script><style>
        li.L0, li.L1, li.L2, li.L3, li.L5, li.L6, li.L7, li.L8 {
            list-style-type: decimal;
        }
    </style>
    <div class="scrollable-content set-padding">
      <div class="container-fluid">
        <div class="row">
          <div class="col-md-12">
            <div class="file-path">
      <span><a href="/LeJit/GPU_Example/browse/">GPU_Example</a> <span class="divider">/</span> </span><span class="active">ConvolutionNN.py <br/> </span>
    </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12">
            
    <div class="row set-padding-bottom">

        <div class="col-sm-12 col-md-6">
            
              <div class="btn-group" role="group">
                
    


<div class="dropdown btn-group">
    <button class="btn btn-primary btn-sm dropdown-toggle" type="button" class="revision-control" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
        
          <span class="message ellipsis">
            
              &ldquo;Generated by Domino&rdquo;
              
          </span>
          <span class="time">
            <span class="timestamp" data-millis="1441317187000"></span>
          </span>
        
        <span class="caret"></span>
    </button>
    <ul class="dropdown-menu" aria-labelledby="revision-control">
        
        <li>
            <a href="/LeJit/GPU_Example/view/ConvolutionNN.py?commitId=f82db8d8d9c8c896bdbcf05f12f1ffb10f793e36">
                <strong class="message ellipsis">
                    
                    &ldquo;Generated by Domino&rdquo;
                    
                </strong>
          <span class="user">
            &ndash;Domino
          </span>
          <span class="time">
            <span class="timestamp" data-millis="1441317187000"></span>
          </span>
            </a>
        </li>
        
        <li>
            <a href="/LeJit/GPU_Example/view/ConvolutionNN.py?commitId=3652c8577077b126f367e01d7be9855b6c40d2e0">
                <strong class="message ellipsis">
                    
                    &ldquo;Generated by Domino&rdquo;
                    
                </strong>
          <span class="user">
            &ndash;LeJit
          </span>
          <span class="time">
            <span class="timestamp" data-millis="1438837485000"></span>
          </span>
            </a>
        </li>
        
        <li>
            <a href="/LeJit/GPU_Example/view/ConvolutionNN.py?commitId=0bc65aec5b4e3ee3bebf8ebbbdf98a49d6eb535f">
                <strong class="message ellipsis">
                    
                    &ldquo;Generated by Domino&rdquo;
                    
                </strong>
          <span class="user">
            &ndash;Domino
          </span>
          <span class="time">
            <span class="timestamp" data-millis="1438837217000"></span>
          </span>
            </a>
        </li>
        
        <li>
            <a href="/LeJit/GPU_Example/view/ConvolutionNN.py?commitId=80383e6ec52e2b5abc32ac5459472ace0d885ee1">
                <strong class="message ellipsis">
                    
                    &ldquo;Generated by Domino&rdquo;
                    
                </strong>
          <span class="user">
            &ndash;LeJit
          </span>
          <span class="time">
            <span class="timestamp" data-millis="1438058362000"></span>
          </span>
            </a>
        </li>
        
    </ul>
</div>


                
              </div>
            
        </div>

        <div class="col-sm-12 col-md-6 align-right">
            <div class="btn-group btn-group-sm">
                <a class="btn btn-primary" href="/LeJit/GPU_Example/edit/ConvolutionNN.py?commitId=f82db8d8d9c8c896bdbcf05f12f1ffb10f793e36">Edit</a>
                
                    <form class="btn-group btn-group-sm" action="/LeJit/GPU_Example/run/start?commitId=f82db8d8d9c8c896bdbcf05f12f1ffb10f793e36" method="POST">
                        <input type="hidden" name="commandToRun" id="commandToRun" value="ConvolutionNN.py">
                        <a class="btn btn-primary btn-sm" href="#" onclick="oneClickSubmit(this, 'Running...');">Run</a>
                    </form>
                
                
                <a class="btn btn-primary" href="/LeJit/GPU_Example/raw/f82db8d8d9c8c896bdbcf05f12f1ffb10f793e36/ConvolutionNN.py?inline=false">Download</a>
                <a class="btn btn-primary" href="/LeJit/GPU_Example/raw/latest/ConvolutionNN.py?inline=true">
                  <span class="inline-help" aria-label="View latest raw file">
                    Raw
                  </span>
                </a>
                <a class="btn btn-primary" href="/LeJit/GPU_Example/compare-revisions/ConvolutionNN.py">
                  <span class="inline-help" aria-label="Compare historical revisions of this file">
                    Compare Revisions
                  </span>
                </a>
            </div>
        </div>

    </div>

          </div>
        </div>
        <div class="row">
          <div class="col-md-12">
            <div id="eN7AhDN1tzFuRbgCvbNkJ2lpgLOUiYGym">
  <div text-center">
    <i class="icon-spinner icon-spin icon-4x"></i><h4>Loading...</h4>
  </div>
</div>
<script>
  $(function () {
    $.ajax({
      url: "/LeJit/GPU_Example/render/ConvolutionNN.py?commitId=f82db8d8d9c8c896bdbcf05f12f1ffb10f793e36&renderUnknownFilesAsText=true",
    }).done(function (data) {
      var $container = $("#eN7AhDN1tzFuRbgCvbNkJ2lpgLOUiYGym");
      $container.html(data);
      var content = $container.children(":first")
      // prettify if required
      if(prettyPrint && content && content.length) {
        prettyPrint(null, $container.get()[0]);
      }
    }).fail(function () {
      $("#eN7AhDN1tzFuRbgCvbNkJ2lpgLOUiYGym").html("<div class='alert alert-danger'>An error occurred while trying to display the file.</div>");
    });
  });
</script>
          </div>
        </div>
        
    <hr />
    <h3>Discussion</h3>
    <div class="row">
        <div class="col-md-12">
            
                


<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {inlineMath: [["$","$"],["\\(","\\)"]]}
  });
</script>
<script type="text/javascript"
        src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

<div id="id-KUxmkn9tLu">

  <div class="comment-group" name="comments-list">





  </div>



    
    
    <input type="hidden" name="comment-context" value="{&quot;_t&quot;:&quot;comments.FileRevisionCommentContext&quot;,&quot;commitId&quot;:&quot;f82db8d8d9c8c896bdbcf05f12f1ffb10f793e36&quot;,&quot;filePath&quot;:{&quot;canonicalizedPathString&quot;:&quot;ConvolutionNN.py&quot;,&quot;separator&quot;:&quot;/&quot;}}">
    <input type="hidden" name="useSmallStyle" value="false" />

    
      <div class="comment-form">
        <div class="set-padding-bottom-small">
            <textarea placeholder="Leave a comment" onkeydown="window.domino.comments.handleCommentFormKeyDown(event, 'id-KUxmkn9tLu')" name="comment-body" class="form-control comment-textarea" rows="5"></textarea>

            <script type="text/javascript">
                $.getJSON("/LeJit/GPU_Example/collaborators", {}, function(usernames) {
                    $("textarea[name=comment-body]").atwho({
                      at: '@',
                      data: usernames
                    })
                });
            </script>
        </div>

        <button class="btn btn-primary btn-sm float-left" name="create-comment-button"
          onClick="window.domino.comments.submitComment('id-KUxmkn9tLu'); return false;">
            Comment
        </button>
        &nbsp;
        <span class="comment-help-link">
            <small>
                <a href="https://help.github.com/articles/markdown-basics/" target="_blank">Markdown</a> and
                <a href="http://docs.mathjax.org/en/latest/start.html#tex-and-latex-input" target="_blank">Mathjax</a> supported. You can also <strong>@mention</strong> people.
            </small>
        </span>
      </div>
    







<script type="text/javascript">
$(function() {
    window.domino = window.domino || {};
    window.domino.comments = window.domino.comments || {};
    window.domino.comments.getCommentData = window.domino.comments.getCommentData || function getCommentData(form, commentBody, commentsList) {
            var lastComment = commentsList.find("[index]").last();
            if (commentBody.length == 0 || commentBody.val() == "") {
                return false;
            }
            var lastIndexShown = -1;
            if (lastComment.length !== 0) {
                lastIndexShown = lastComment.attr("index");
            }
            var contextKey = form.find(":input[name=comment-context]");
            var useSmallStyle = form.find(":input[name=useSmallStyle]");
            var dataPost = { };
            dataPost["comment-body"] = commentBody.val();
            dataPost["comment-context"] = contextKey.val();
            dataPost["last-comment-index-shown"] = lastIndexShown;
            dataPost["useSmallStyle"] = useSmallStyle.val();
            return dataPost;
    };

    window.domino.comments.submitComment = window.domino.comments.submitComment || function submitComment(formId) {
            var form = $("#" + formId);
            var commentBody = form.find("[name=comment-body]");
            var commentsList = form.find("[name=comments-list]");
            var url = "/LeJit/GPU_Example/comments";
            var commentData = window.domino.comments.getCommentData(form, commentBody, commentsList);
            var request = $.ajax({
                type: "POST",
                url: url,
                data: commentData
            });
            request.done(function(data) {
                commentBody.val("");
                var newHTMLContainer = $("<div></div>").appendTo(commentsList).hide().append(data);
                newHTMLContainer.fadeIn("slow");
                MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
                window.domino.utils.renderTimestamps();
            });
            request.fail(function(jqXHR, textStatus) {
                if ((jqXHR.status === 401) || (jqXHR.status === 403)) {
                    UserAlert.error("You are not authorized to create comments in this project.");
                } else {
                    UserAlert.error("Comment could not be saved. Please try again later.");
                }
            });
    };

    window.domino.comments.handleCommentFormKeyDown = window.domino.comments.handleCommentFormKeyDown || function handleCommentFormKeyDown(event, formId) {
            var createCommentButton = $("#" + formId + " [name=create-comment-button]");
            if ((event.ctrlKey || event.metaKey) && event.keyCode == 13) {
                // Ctrl-Enter / Command-Enter pressed
                createCommentButton.click();
            } else if (event.keyCode == 9) {
                // Tab pressed
                event.preventDefault();
                createCommentButton.focus();
            }
    };
});
</script>
</div>


                <div class="set-padding-top">
                
                </div>
            
        </div>

    </div>

      </div>
    </div>
    


                    
                </div>
            </div>
        </div>

        



    


        
            

<script>
  $(function() {
    $(document).on("click", "#startThisRunBtn", function (e) {
      e.preventDefault();
      var self = $(this);
      var commandToRunString = self.data('name');

      $("#commandToRunModalTitle").text(" Run " + commandToRunString + "?");
      $("#acceptBtn").attr("data-name", commandToRunString);
      $("#commandToRunInput").val(commandToRunString);

      $(self.attr('href')).modal('show');
    });
  });
</script>


  <script>
    $(function() {
      $(document).on("click", "#acceptBtn", function (e) {
        $(this).closest('form').submit(); return false;
      });
    });
  </script>


<div class="modal fade" id="runConfirmationModal" role="dialog" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                <h3 class="modal-title" id="commandToRunModalTitle"></h3>
            </div>
            <div class="modal-body">
                This will run the file from an older project state. Are you sure you want to continue?
            </div>
            <div class="modal-footer">
              <form action="/LeJit/GPU_Example/run/start?commitId=f82db8d8d9c8c896bdbcf05f12f1ffb10f793e36" method="POST">
                <input type="hidden" name="commandToRun" id="commandToRunInput" value="" />

                <button class="btn btn-default" data-dismiss="modal">Cancel</button>
                <a class="btn btn-primary" id="acceptBtn"><i class="glyphicon glyphicon-play"></i> Run</a>
              </form>
            </div>
        </div>
    </div>
</div>

        
            
    <div id="fork-modal" role="dialog" class="modal fade">
        <div class="modal-dialog">
            <div class="modal-content">

                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                    <h3 class="modal-title"><i class="icon-code-fork"></i> Fork <code>LeJit/GPU_Example</code></h3>
                </div>

                
                    <div class="modal-body">
                        <div class="alert alert-danger">
                            You need to be logged in in order to fork a project. Please <a href="/signup">
                            create an account</a> and try again.
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button class="btn btn-default" data-dismiss="modal">Cancel</button>
                        <a class="btn btn-primary" href="/signup">Sign up</a>
                    </div>
                
            </div>
        </div>

    </div>

        
    </body>
</html>


























































