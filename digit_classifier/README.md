



<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    

    <link crossorigin="anonymous" href="https://github.kdc.capitalone.com/assets/frameworks-dfef81085aa6db7d34192121ecd8243fdef5dbe4934bada47df1eb58307020fb.css" media="all" rel="stylesheet" />
    <link crossorigin="anonymous" href="https://github.kdc.capitalone.com/assets/github-068b9a6374f2a7865aa3407f2e8315caeda66d28d7d8df04d9ed7045b479c0e0.css" media="all" rel="stylesheet" />
    
    
    <link crossorigin="anonymous" href="https://github.kdc.capitalone.com/assets/site-f6ce114ac3bc145f575863b4a6dbdf65e924bccb184fc4d4a4f5a09819b4173d.css" media="all" rel="stylesheet" />
    

    <link as="script" href="https://github.kdc.capitalone.com/assets/frameworks-fd8c4a749a04d1f8028ff32d7c1386ec583ac2e63db7ff9801898fca7013d345.js" rel="preload" />
    
    <link as="script" href="https://github.kdc.capitalone.com/assets/github-27b71033de6a2b1e2505b2650bb6152f9fe3c4078a7b1ec7ee777da095327305.js" rel="preload" />

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="viewport" content="width=device-width">
    
    <title>deepseries/README.md at master · ezw112/deepseries · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.kdc.capitalone.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="/apple-touch-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="/apple-touch-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="/apple-touch-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="/apple-touch-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon-180x180.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="https://github.kdc.capitalone.com/avatars/u/1427?s=400" name="twitter:image:src" /><meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="ezw112/deepseries" name="twitter:title" /><meta content="deepseries - Deep learning applications for prediction of time series" name="twitter:description" />
      <meta content="https://github.kdc.capitalone.com/avatars/u/1427?s=400" property="og:image" /><meta content="GitHub Enterprise" property="og:site_name" /><meta content="object" property="og:type" /><meta content="ezw112/deepseries" property="og:title" /><meta content="https://github.kdc.capitalone.com/ezw112/deepseries" property="og:url" /><meta content="deepseries - Deep learning applications for prediction of time series" property="og:description" />
    <meta name="browser-errors-url" content="https://github.kdc.capitalone.com/api/v3/_private/browser/errors">
    <link rel="assets" href="https://github.kdc.capitalone.com/">
    
    <meta name="pjax-timeout" content="1000">
    
    <meta name="request-id" content="a512dd61-19f3-48d3-b92b-466db2f20227" data-pjax-transient>

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">


<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />



  <meta class="js-ga-set" name="dimension1" content="Logged Out">



        <meta name="hostname" content="enterprise.host">
    <meta name="user-login" content="">



      <link rel="mask-icon" href="https://github.kdc.capitalone.com/pinned-octocat.svg" color="#4078c0">
      <link rel="icon" type="image/x-icon" href="https://github.kdc.capitalone.com/favicon-enterprise.ico">

    <meta name="html-safe-nonce" content="f8c9465de9e249c4fecded44fa5ba0f52330cd7c">
    <meta content="e13c021d104ce5d70aa3c5bd50d5cd0021fff33d" name="form-nonce" />

    <meta http-equiv="x-pjax-version" content="1ecfa1035f7967301570c75b996a48ce">
    

      
  <meta name="description" content="deepseries - Deep learning applications for prediction of time series">
  <meta name="go-import" content="github.kdc.capitalone.com/ezw112/deepseries git https://github.kdc.capitalone.com/ezw112/deepseries.git">

  
  <link href="https://github.kdc.capitalone.com/ezw112/deepseries/commits/master.atom" rel="alternate" title="Recent Commits to deepseries:master" type="application/atom+xml">


      <link rel="canonical" href="https://github.kdc.capitalone.com/ezw112/deepseries/blob/master/examples/simple_classification/README.md" data-pjax-transient>
  </head>


  <body class="logged-out enterprise env-production  vis-public page-blob">
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>

    
    
    



          <div class="header header-logged-out" role="banner">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.kdc.capitalone.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
      <svg aria-hidden="true" class="octicon octicon-logo-github" height="28" version="1.1" viewBox="0 0 45 16" width="78"><path d="M18.53 12.03h-.02c.009 0 .015.01.024.011h.006l-.01-.01zm.004.011c-.093.001-.327.05-.574.05-.78 0-1.05-.36-1.05-.83V8.13h1.59c.09 0 .16-.08.16-.19v-1.7c0-.09-.08-.17-.16-.17h-1.59V3.96c0-.08-.05-.13-.14-.13h-2.16c-.09 0-.14.05-.14.13v2.17s-1.09.27-1.16.28c-.08.02-.13.09-.13.17v1.36c0 .11.08.19.17.19h1.11v3.28c0 2.44 1.7 2.69 2.86 2.69.53 0 1.17-.17 1.27-.22.06-.02.09-.09.09-.16v-1.5a.177.177 0 0 0-.146-.18zm23.696-2.2c0-1.81-.73-2.05-1.5-1.97-.6.04-1.08.34-1.08.34v3.52s.49.34 1.22.36c1.03.03 1.36-.34 1.36-2.25zm2.43-.16c0 3.43-1.11 4.41-3.05 4.41-1.64 0-2.52-.83-2.52-.83s-.04.46-.09.52c-.03.06-.08.08-.14.08h-1.48c-.1 0-.19-.08-.19-.17l.02-11.11c0-.09.08-.17.17-.17h2.13c.09 0 .17.08.17.17v3.77s.82-.53 2.02-.53l-.01-.02c1.2 0 2.97.45 2.97 3.88zm-8.72-3.61H33.84c-.11 0-.17.08-.17.19v5.44s-.55.39-1.3.39-.97-.34-.97-1.09V6.25c0-.09-.08-.17-.17-.17h-2.14c-.09 0-.17.08-.17.17v5.11c0 2.2 1.23 2.75 2.92 2.75 1.39 0 2.52-.77 2.52-.77s.05.39.08.45c.02.05.09.09.16.09h1.34c.11 0 .17-.08.17-.17l.02-7.47c0-.09-.08-.17-.19-.17zm-23.7-.01h-2.13c-.09 0-.17.09-.17.2v7.34c0 .2.13.27.3.27h1.92c.2 0 .25-.09.25-.27V6.23c0-.09-.08-.17-.17-.17zm-1.05-3.38c-.77 0-1.38.61-1.38 1.38 0 .77.61 1.38 1.38 1.38.75 0 1.36-.61 1.36-1.38 0-.77-.61-1.38-1.36-1.38zm16.49-.25h-2.11c-.09 0-.17.08-.17.17v4.09h-3.31V2.6c0-.09-.08-.17-.17-.17h-2.13c-.09 0-.17.08-.17.17v11.11c0 .09.09.17.17.17h2.13c.09 0 .17-.08.17-.17V8.96h3.31l-.02 4.75c0 .09.08.17.17.17h2.13c.09 0 .17-.08.17-.17V2.6c0-.09-.08-.17-.17-.17zM8.81 7.35v5.74c0 .04-.01.11-.06.13 0 0-1.25.89-3.31.89-2.49 0-5.44-.78-5.44-5.92S2.58 1.99 5.1 2c2.18 0 3.06.49 3.2.58.04.05.06.09.06.14L7.94 4.5c0 .09-.09.2-.2.17-.36-.11-.9-.33-2.17-.33-1.47 0-3.05.42-3.05 3.73s1.5 3.7 2.58 3.7c.92 0 1.25-.11 1.25-.11v-2.3H4.88c-.11 0-.19-.08-.19-.17V7.35c0-.09.08-.17.19-.17h3.74c.11 0 .19.08.19.17z"></path></svg>
    </a>

    <div class="header-actions" role="navigation">
      <a class="btn" href="/login?return_to=%2Fezw112%2Fdeepseries%2Fblob%2Fmaster%2Fexamples%2Fsimple_classification%2FREADME.md" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
    </div>

    <div class="site-search scoped-search js-site-search" role="search">
      <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/ezw112/deepseries/search" class="js-site-search-form" data-scoped-search-url="/ezw112/deepseries/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
      <div class="header-search-scope">This repository</div>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
    </label>
</form></div>

    </div>

      <ul class="header-nav float-left" role="navigation">
          <li class="header-nav-item">
            <a class="header-nav-link" href="/explore" data-ga-click="(Logged out) Header, go to explore, text:explore">Explore</a>
          </li>
      </ul>

  </div>
</div>



    <div id="start-of-content" class="accessibility-aid"></div>

      <div id="js-flash-container">
</div>


    <div role="main">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
      
<div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
  <div class="container repohead-details-container">

    

<ul class="pagehead-actions">

  <li>
      <a href="/login?return_to=%2Fezw112%2Fdeepseries"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
    Watch
  </a>
  <a class="social-count" href="/ezw112/deepseries/watchers"
     aria-label="4 users are watching this repository">
    4
  </a>

  </li>

  <li>
      <a href="/login?return_to=%2Fezw112%2Fdeepseries"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"></path></svg>
    Star
  </a>

    <a class="social-count js-social-count" href="/ezw112/deepseries/stargazers"
      aria-label="3 users starred this repository">
      3
    </a>

  </li>

  <li>
      <a href="/login?return_to=%2Fezw112%2Fdeepseries"
        class="btn btn-sm btn-with-count tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
        Fork
      </a>

    <a href="/ezw112/deepseries/network" class="social-count"
       aria-label="3 users are forked this repository">
      3
    </a>
  </li>
</ul>

    <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"></path></svg>
  <span class="author" itemprop="author"><a href="/ezw112" class="url fn" rel="author">ezw112</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/ezw112/deepseries" data-pjax="#js-repo-pjax-container">deepseries</a></strong>

</h1>

  </div>
  <div class="container">
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/ezw112/deepseries" aria-selected="true" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /ezw112/deepseries" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"></path></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/ezw112/deepseries/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /ezw112/deepseries/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
        <span itemprop="name">Issues</span>
        <span class="counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/ezw112/deepseries/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /ezw112/deepseries/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
      <span itemprop="name">Pull requests</span>
      <span class="counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>

  <a href="/ezw112/deepseries/projects" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /ezw112/deepseries/projects">
    <svg class="octicon" aria-hidden="true" version="1.1" width="15" height="16" viewBox="0 0 15 16">
      <path d="M1 15h13V1H1v14zM15 1v14a1 1 0 0 1-1 1H1a1 1 0 0 1-1-1V1a1 1 0 0 1 1-1h13a1 1 0 0 1 1 1zm-4.41 11h1.82c.59 0 .59-.41.59-1V3c0-.59 0-1-.59-1h-1.82C10 2 10 2.41 10 3v8c0 .59 0 1 .59 1zm-4-2h1.82C9 10 9 9.59 9 9V3c0-.59 0-1-.59-1H6.59C6 2 6 2.41 6 3v6c0 .59 0 1 .59 1zM2 13V3c0-.59 0-1 .59-1h1.82C5 2 5 2.41 5 3v10c0 .59 0 1-.59 1H2.59C2 14 2 13.59 2 13z"></path>
    </svg>
    Projects
    <span class="counter">0</span>
</a>


  <a href="/ezw112/deepseries/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="pulse /ezw112/deepseries/pulse">
    <svg aria-hidden="true" class="octicon octicon-pulse" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M11.5 8L8.8 5.4 6.6 8.5 5.5 1.6 2.38 8H0v2h3.6l.9-1.8.9 5.4L9 8.5l1.6 1.5H14V8z"></path></svg>
    Pulse
</a>
  <a href="/ezw112/deepseries/graphs" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors /ezw112/deepseries/graphs">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"></path></svg>
    Graphs
</a>

</nav>

  </div>
</div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    

<a href="/ezw112/deepseries/blob/844fe8a216018927028cd1ac6518e5f553c419ab/examples/simple_classification/README.md" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:736ceece63165ab9fa0d15832d9f9cca -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <i>Branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/ezw112/deepseries/blob/master/examples/simple_classification/README.md"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ezw112/deepseries/blob/original_stable/examples/simple_classification/README.md"
               data-name="original_stable"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                original_stable
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="BtnGroup float-right">
    <a href="/ezw112/deepseries/find/master"
          class="js-pjax-capture-input btn btn-sm BtnGroup-item"
          data-pjax
          data-hotkey="t">
      Find file
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
  </div>
  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/ezw112/deepseries"><span>deepseries</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a href="/ezw112/deepseries/tree/master/examples"><span>examples</span></a></span><span class="separator">/</span><span class="js-path-segment"><a href="/ezw112/deepseries/tree/master/examples/simple_classification"><span>simple_classification</span></a></span><span class="separator">/</span><strong class="final-path">README.md</strong>
  </div>
</div>


  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/ezw112/deepseries/commit/ca7c940da6efa5cb1baa659bea9a5fe4ea97ef13" data-pjax>
          ca7c940
        </a>
        <relative-time datetime="2016-10-31T19:45:13Z">Oct 31, 2016</relative-time>
      </span>
      <div>
        <img alt="@ezw112" class="avatar" height="20" src="https://github.kdc.capitalone.com/avatars/u/1427?s=40" width="20" />
        <a href="/ezw112" class="user-mention" rel="author">ezw112</a>
          <a href="/ezw112/deepseries/commit/ca7c940da6efa5cb1baa659bea9a5fe4ea97ef13" class="message" data-pjax="true" title="adding installer">adding installer</a>
      </div>

    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>1</strong>
         contributor
      </button>
      
    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@ezw112" height="24" src="https://github.kdc.capitalone.com/avatars/u/1427?s=48" width="24" />
            <a href="/ezw112">ezw112</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a href="/ezw112/deepseries/raw/master/examples/simple_classification/README.md" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/ezw112/deepseries/blame/master/examples/simple_classification/README.md" class="btn btn-sm js-update-url-with-hash BtnGroup-item">Blame</a>
      <a href="/ezw112/deepseries/commits/master/examples/simple_classification/README.md" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>


        <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"></path></svg>
        </button>
        <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"></path></svg>
        </button>
  </div>

  <div class="file-info">
      153 lines (109 sloc)
      <span class="file-info-divider"></span>
    3.84 KB
  </div>
</div>

  
  <div id="readme" class="readme blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="text"><h1><a id="user-content-simple-classification-of-time-series-with-deepseries" class="anchor" href="#simple-classification-of-time-series-with-deepseries" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Simple classification of time series with DeepSeries</h1>

<h3><a id="user-content-in-this-example-train-a-classifier-with-a-public-data-set-of-labeled-numerical-time-series" class="anchor" href="#in-this-example-train-a-classifier-with-a-public-data-set-of-labeled-numerical-time-series" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>In this example train a classifier with a public data set of labeled numerical time series.</h3>

<h3><a id="user-content-a-description-of-the-data-and-labels-can-be-found-here-httpkddicsuciedudatabasessynthetic_controlsynthetic_controldatahtml" class="anchor" href="#a-description-of-the-data-and-labels-can-be-found-here-httpkddicsuciedudatabasessynthetic_controlsynthetic_controldatahtml" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>A description of the data and labels can be found here: <a href="http://kdd.ics.uci.edu/databases/synthetic_control/synthetic_control.data.html">http://kdd.ics.uci.edu/databases/synthetic_control/synthetic_control.data.html</a></h3>

<h3><a id="user-content-it-consists-of-600-sequences-with-60-time-steps-each-there-are-6-labeled-kinds-of-sequences" class="anchor" href="#it-consists-of-600-sequences-with-60-time-steps-each-there-are-6-labeled-kinds-of-sequences" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>It consists of 600 sequences with 60 time steps each. There are 6 labeled kinds of sequences.</h3>

<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> numpy <span class="pl-k">as</span> np
<span class="pl-k">import</span> pandas <span class="pl-k">as</span> pd
<span class="pl-k">from</span> sklearn.preprocessing <span class="pl-k">import</span> OneHotEncoder
<span class="pl-k">import</span> os, sys
<span class="pl-k">from</span> deepseries <span class="pl-k">import</span> deepseries, preprocessing</pre></div>

<div class="highlight highlight-source-python"><pre><span class="pl-c"># Load data and scale each series so that its min/max are [-0.5,0.5]</span>
df <span class="pl-k">=</span> pd.read_pickle(<span class="pl-s"><span class="pl-pds">'</span>ts_data.pkl<span class="pl-pds">'</span></span>)
df <span class="pl-k">=</span> df <span class="pl-k">-</span> df.min()
df <span class="pl-k">=</span> df<span class="pl-k">/</span>df.max() <span class="pl-k">-</span> <span class="pl-c1">0.5</span></pre></div>

<div class="highlight highlight-source-python"><pre><span class="pl-c"># Build an array of one-hot encoded labels</span>
labels <span class="pl-k">=</span> df.index.values
enc <span class="pl-k">=</span> OneHotEncoder()
enc.fit([[l] <span class="pl-k">for</span> l <span class="pl-k">in</span> <span class="pl-c1">set</span>(labels)])
onehot_labels <span class="pl-k">=</span> enc.transform(labels.reshape(<span class="pl-k">-</span><span class="pl-c1">1</span>,<span class="pl-c1">1</span>)).toarray()</pre></div>

<div class="highlight highlight-source-python"><pre><span class="pl-c"># Reshape labels (y) and data (X) to</span>
<span class="pl-c"># (Nsequences=600, sequence_length=60, Nchannels=1) for X</span>
<span class="pl-c"># (Nsequences=600, sequence_length=1, Nchannels=6) for y</span>
y <span class="pl-k">=</span> onehot_labels.reshape(<span class="pl-c1">600</span>,<span class="pl-c1">1</span>,<span class="pl-c1">6</span>)
<span class="pl-c1">X</span> <span class="pl-k">=</span> df.values.reshape(<span class="pl-c1">600</span>,<span class="pl-c1">60</span>,<span class="pl-c1">1</span>)</pre></div>

<div class="highlight highlight-source-python"><pre><span class="pl-c"># Train-test split. Test data are the trailing 20% of samples</span>
split_idx <span class="pl-k">=</span> <span class="pl-c1">int</span>(<span class="pl-c1">0.8</span><span class="pl-k">*</span><span class="pl-c1">X</span>.shape[<span class="pl-c1">0</span>])
Xtrain, Xtest, ytrain, ytest <span class="pl-k">=</span>  <span class="pl-c1">X</span>[:split_idx], <span class="pl-c1">X</span>[split_idx:], y[:split_idx], y[split_idx:]</pre></div>

<div class="highlight highlight-source-python"><pre><span class="pl-c"># Initialize classifier</span>
dsc <span class="pl-k">=</span> deepseries.many2oneClassifier(
    Xtrain,
    ytrain,
    Xtest,
    ytest,
    <span class="pl-v">Nnodes</span><span class="pl-k">=</span><span class="pl-c1">50</span>,
    <span class="pl-v">Nlayers</span><span class="pl-k">=</span><span class="pl-c1">2</span>,
    <span class="pl-v">optimizer_type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>AdamOptimizer<span class="pl-pds">'</span></span>,
    <span class="pl-v">optimizer_kwargs</span><span class="pl-k">=</span>{<span class="pl-s"><span class="pl-pds">'</span>learning_rate<span class="pl-pds">'</span></span>:<span class="pl-c1">0.001</span>},
    <span class="pl-v">batch_size</span><span class="pl-k">=</span><span class="pl-c1">40</span>,
    <span class="pl-v">tracking_step</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</pre></div>

<div class="highlight highlight-source-python"><pre><span class="pl-c"># Fit classifier</span>
dsc.fit(<span class="pl-v">n_epochs</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</pre></div>

<pre><code>train batch cost: 67.970, test cost: 202.590
train batch cost: 42.592, test cost: 114.336
train batch cost: 28.770, test cost: 70.614
train batch cost: 18.250, test cost: 48.772
train batch cost: 15.075, test cost: 46.274
train batch cost: 14.529, test cost: 31.100
train batch cost: 5.646, test cost: 37.048
train batch cost: 7.171, test cost: 33.351
train batch cost: 6.589, test cost: 26.185
train batch cost: 11.323, test cost: 35.252
train batch cost: 5.731, test cost: 24.785
train batch cost: 7.095, test cost: 25.040
train batch cost: 3.395, test cost: 26.016
train batch cost: 5.241, test cost: 23.565
train batch cost: 9.701, test cost: 27.982
train batch cost: 6.283, test cost: 29.715
train batch cost: 5.597, test cost: 24.245
train batch cost: 4.041, test cost: 22.840
train batch cost: 3.276, test cost: 18.048
train batch cost: 1.283, test cost: 21.016
</code></pre>

<div class="highlight highlight-source-python"><pre><span class="pl-c"># Compute accuracy</span>
dsc.classification_accuracy()</pre></div>

<pre><code>0.94999999
</code></pre>

<h3><a id="user-content-the-classifier-achieves-around-95-accuracy-on-this-6-label-classification-this-performance-is-good-considering-the-small-size-of-the-data-set" class="anchor" href="#the-classifier-achieves-around-95-accuracy-on-this-6-label-classification-this-performance-is-good-considering-the-small-size-of-the-data-set" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>The classifier achieves around 95% accuracy on this 6-label classification. This performance is good considering the small size of the data set.</h3>

<div class="highlight highlight-source-python"><pre><span class="pl-c"># To return predictions in one-hot encoded form:</span>
predictions_onehot <span class="pl-k">=</span> dsc.predict(Xtest)
<span class="pl-c1">print</span> predictions_onehot[:<span class="pl-c1">3</span>]</pre></div>

<pre><code>[[[0 0 0 0 1 0]]

 [[0 0 0 0 1 0]]

 [[1 0 0 0 0 0]]]
</code></pre>

<div class="highlight highlight-source-python"><pre><span class="pl-c"># To return predicted labels as sequential integers (e.g., the way they were before one-hot enconding in our case):</span>
predictions <span class="pl-k">=</span> dsc.predict(Xtest, <span class="pl-v">return_class_indices</span><span class="pl-k">=</span><span class="pl-c1">True</span>)
<span class="pl-c1">print</span> predictions[:<span class="pl-c1">3</span>]</pre></div>

<pre><code>[[4]
 [4]
 [0]]
</code></pre>

<div class="highlight highlight-source-python"><pre><span class="pl-c"># You also might want to output the softmax probabilities.</span>
<span class="pl-c"># These are the probability distributions, P(Class_i|Sample_k), and are</span>
<span class="pl-c"># normalized to 1 for every sample:</span>
probabilities <span class="pl-k">=</span> dsc.predict_proba(Xtest)
<span class="pl-c1">print</span> probabilities[:<span class="pl-c1">3</span>]</pre></div>

<pre><code>[[[  8.18560249e-04   4.89840677e-05   1.11215631e-03   6.32073011e-07
     9.98018861e-01   8.06433150e-07]]

 [[  8.60203363e-05   1.69548930e-05   8.69577343e-05   6.57956676e-08
     9.99810040e-01   2.27038335e-08]]

 [[  9.92291152e-01   4.66434238e-03   1.82475094e-04   4.42926335e-04
     2.28498410e-03   1.34180547e-04]]]
</code></pre>
</article>
  </div>

</div>

<button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
<div id="jump-to-line" style="display:none">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>


    </div>
  </div>

    </div>

        <div class="container site-footer-container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links float-right">
      <li><a href="https://developer.github.com/enterprise/2.8" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog">Blog</a></li>
        <li><a href="https://github.com/about">About</a></li>

    </ul>

    <a href="https://github.kdc.capitalone.com" aria-label="Homepage" class="site-footer-mark" title="GitHub Enterprise">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2017 <span title="0.06756s from localhost">GitHub</span>, Inc.</li>
        <li><a href="https://help.github.com/enterprise/2.8">Help</a></li>
        <li><a href="mailto:github.admins@capitalone.com">Support</a></li>
    </ul>
  </div>
</div>



    

    <div id="ajax-error-message" class="ajax-error-message flash flash-error">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"></path></svg>
      <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
        <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
      </button>
      You can't perform that action at this time.
    </div>


      <script crossorigin="anonymous" src="https://github.kdc.capitalone.com/assets/compat-abaa4c7f42b9672df700d2ac49e945d8a83c152564128aa187059c254c75eabd.js"></script>
      <script crossorigin="anonymous" src="https://github.kdc.capitalone.com/assets/frameworks-fd8c4a749a04d1f8028ff32d7c1386ec583ac2e63db7ff9801898fca7013d345.js"></script>
      <script async="async" crossorigin="anonymous" src="https://github.kdc.capitalone.com/assets/github-27b71033de6a2b1e2505b2650bb6152f9fe3c4078a7b1ec7ee777da095327305.js"></script>
      
      
      
      
      
      
    <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"></path></svg>
      <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
      <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
    <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
    </button>
  </div>
</div>

  </body>
</html>

