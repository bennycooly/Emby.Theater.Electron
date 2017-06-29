{
  "targets":
  [
    {
      "target_name": "libcec",
      "sources":
      [
        "cec/addon/libcec.cc"
      ],
      "include_dirs":
      [
        "<!@(node -p \"require('node-addon-api').include\")",
        "cec/libcec/include"
      ],
      "dependencies":
      [
        "<!(node -p \"require('node-addon-api').gyp\")"
      ],   
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],

      "conditions":
      [
        [
          "OS == 'win'",
          {
            "link_settings":
            {
              "library_dirs":
              [
                "cec/libcec/windows/cec"
              ]
            },
            "msbuild_toolset": "v141",
            "msvs_settings":
            {
              "VCCLCompilerTool":
              {
                "ExceptionHandling": 1
              }
            }
          }
        ],
        [
          "OS == 'mac'",
          {
            "xcode_settings":
            {
              "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
              "CLANG_CXX_LIBRARY": "libc++",
              "MACOSX_DEPLOYMENT_TARGET": "10.7"
            }
          }
        ]
      ]
      
    }
  ]
}
