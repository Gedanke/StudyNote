	?;Fz?@?;Fz?@!?;Fz?@	??SF?? @??SF?? @!??SF?? @"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$?;Fz?@?30?????ADR%????Y?^a?????*	(1??M@2F
Iterator::Model??_̖???!d?g?F@)m;m?Ƒ?1^@?-a=@:Preprocessing2j
3Iterator::Model::ParallelMap::Zip[1]::ForeverRepeatI???*ݍ?!c?????8@)<i??
??1»R=?Y6@:Preprocessing2d
-Iterator::Model::ParallelMap::Zip[0]::FlatMapڬ?\mŎ?!œ漚n9@)?@?v??1?PC'?74@:Preprocessing2S
Iterator::Model::ParallelMap-?}́?!??}E?l-@)-?}́?1??}E?l-@:Preprocessing2X
!Iterator::Model::ParallelMap::Zip????N???!?? ???K@)j?!?
l?1?x???,@:Preprocessing2t
=Iterator::Model::ParallelMap::Zip[0]::FlatMap[0]::TensorSlice???GS=i?!??V6?@)???GS=i?1??V6?@:Preprocessing2v
?Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat::FromTensor-??;??V?!???@)-??;??V?1???@:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
device?Your program is NOT input-bound because only 2.1% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*high2B41.9 % of the total step time sampled is spent on All Others time.#You may skip the rest of this page.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	?30??????30?????!?30?????      ??!       "      ??!       *      ??!       2	DR%????DR%????!DR%????:      ??!       B      ??!       J	?^a??????^a?????!?^a?????R      ??!       Z	?^a??????^a?????!?^a?????JCPU_ONLY